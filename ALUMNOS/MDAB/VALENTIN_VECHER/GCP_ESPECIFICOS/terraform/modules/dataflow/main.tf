# resource "null_resource" "build_and_push_docker_dataflow" {
#     provisioner "local-exec" {
#         working_dir = path.module
#         command= <<-EOT
#             docker build --platform=linuz/amd64 -t ${var.image_name_dataflow}:latest -f ${var.dataflow_path_to_image} $(dirname ${var.dataflow_path_to_image})
#             docker tag ${var.image_name_dataflow}:latest ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_dataflow}/dataflow-pipeline:latest
#             docker push ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_dataflow}/dataflow-pipeline:latest
#        EOT
#     }
# }

# resource "null_resource" "build_flex_template" {
#     depends_on = [null_resource.build_and_push_docker_dataflow]

#     provisioner "local-exec" {
#         working_dir = path.module
#         command = <<-EOT
#             gcloud dataflow flex-template build gs://${google_storage_bucket.dataflow_bucket.name}/templates/flex_template.json --image ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_dataflow}/dataflow-pipeline:latest --sdk-language PYTHON --temp-location gs://${google_storage_bucket.dataflow_bucket.name}/temp --staging-location gs://${google_storage_bucket.dataflow_bucket.name}/staging || (echo Error al construir la flex template & exit /b 1)
#         EOT
#     }
# }

# resource "time_sleep" "wait_for_template" {
#     depends_on = [null_resource.build_flex_template]
#     create_duration = "40s"
# }

# resource "google_dataflow_flex_template_job" "dataflow_job_template" {
#     provider = google-beta
#     depends_on = [null_resource.build_and_push_docker_dataflow, null_resource.build_flex_template , google_storage_bucket.dataflow_bucket , time_sleep.wait_for_template]
#     name = var.dataflow_job_name
#     region = var.region 
#     container_spec_gcs_path = "gs://${google_storage_bucket.dataflow_bucket_name}/templates/flex_template.json"
    
#     on_delete = "cancel"
 
# }