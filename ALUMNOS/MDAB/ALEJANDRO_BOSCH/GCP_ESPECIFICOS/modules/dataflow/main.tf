# Bucket para almacenar la flex template
resource "google_storage_bucket" "template_bucket" {
  name     = var.bucket_name
  location = var.location
  force_destroy = true  
}

resource "null_resource" "build_and_push_image" {
  provisioner "local-exec" {
    interpreter = ["cmd", "/c"]
    command = <<EOT
gcloud auth configure-docker ${var.region}-docker.pkg.dev --quiet && docker build --platform linux/amd64 -t dataflow-temp ${var.build_context_dir} && docker tag dataflow-temp ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_id}/dataflow-pipeline:latest && docker push ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_id}/dataflow-pipeline:latest || (echo Error al subir la imagen Docker & exit /b 1)
EOT
  }
}



resource "null_resource" "build_flex_template" {
  depends_on = [google_storage_bucket.template_bucket, null_resource.build_and_push_image]
  
  provisioner "local-exec" {
    interpreter = ["cmd", "/c"]
    command = <<EOT
gcloud dataflow flex-template build gs://${google_storage_bucket.template_bucket.name}/templates/flex_template.json --image ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_id}/dataflow-pipeline:latest --sdk-language PYTHON --temp-location gs://${google_storage_bucket.template_bucket.name}/temp --staging-location gs://${google_storage_bucket.template_bucket.name}/staging || (echo Error al construir la flex template & exit /b 1)
EOT
  }
}

resource "time_sleep" "wait_for_template" {
  depends_on = [null_resource.build_flex_template]
  create_duration = "30s"
}


resource "google_dataflow_flex_template_job" "dataflow_job" {
  provider = google-beta
  depends_on = [null_resource.build_and_push_image, null_resource.build_flex_template, google_storage_bucket.template_bucket, time_sleep.wait_for_template, google_storage_bucket.template_bucket]
 
  name                    = var.dataflow_job_name
  region                  = var.region
  container_spec_gcs_path = "gs://${google_storage_bucket.template_bucket.name}/templates/flex_template.json"
   
  # Añadir tiempos de espera más largos
  on_delete = "cancel"
 
  parameters = {
    project_id                         = var.project_id
    battery_telemetry_subscription     = var.battery_telemetry_subscription
    driving_telemetry_subscription     = var.driving_telemetry_subscription
    environment_telemetry_subscription = var.environment_telemetry_subscription
    firestore_collection               = var.firestore_collection
    output_topic                       = var.output_topic
    image_api                          = var.image_api
   
    temp_location                      = "gs://${google_storage_bucket.template_bucket.name}/temp"
    staging_location                   = "gs://${google_storage_bucket.template_bucket.name}/staging"
  }
}
