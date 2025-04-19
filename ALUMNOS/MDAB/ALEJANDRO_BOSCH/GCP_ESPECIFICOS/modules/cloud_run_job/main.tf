resource "null_resource" "docker_push" {
  provisioner "local-exec" {
    command = <<EOT
docker build --platform linux/amd64 -t generators ${var.build_context_dir} && docker tag generators europe-west1-docker.pkg.dev/${var.project_id}/${var.artifact_registry_repository}/generators:${var.tag} && docker push europe-west1-docker.pkg.dev/${var.project_id}/${var.artifact_registry_repository}/generators:${var.tag} || { echo "Error al subir la imagen Docker"; exit 1; }
EOT
  }
}


resource "google_cloud_run_v2_job" "vehicle_data_job" {
  depends_on = [null_resource.docker_push]
 
  name     = "vehicle-data-job"
  location = var.region
  template {
    task_count = 1
    template {
      service_account = google_service_account.job_service_account.email
      
      containers {
        image = "${var.image_repository}:${var.image_tag}"
        args = [
          "--project_id", var.project_id,
          "--telemetry_battery_topic", var.telemetry_battery_topic,
          "--telemetry_driving_topic", var.telemetry_driving_topic,
          "--telemetry_environment_topic", var.telemetry_environment_topic,
          "--city_name", var.city_name,
        ]
      }
    }
  }
  deletion_protection = false
}




resource "null_resource" "execute_vehicle_data_job" {
  depends_on = [
    google_cloud_run_v2_job.vehicle_data_job
  ]

  provisioner "local-exec" {
    command = <<EOT
gcloud beta run jobs execute vehicle-data-job --region ${var.region} --project ${var.project_id}
EOT
  }
}

resource "google_service_account" "job_service_account" {
  account_id   = "job-service-account"
  display_name = "Service account for Cloud Run Job"
}

resource "google_project_iam_member" "pubsub_publisher" {
  project = var.project_id
  role    = "roles/pubsub.publisher"
  member  = "serviceAccount:${google_service_account.job_service_account.email}"
}

resource "null_resource" "docker_push_bq" {
  provisioner "local-exec" {
    command = <<EOT
docker build --platform linux/amd64 -t firestore-to-bq ${var.build_context_dir_bq} && docker tag firestore-to-bq europe-west1-docker.pkg.dev/${var.project_id}/${var.artifact_registry_repository}/firestore-to-bq:${var.tag} && docker push europe-west1-docker.pkg.dev/${var.project_id}/${var.artifact_registry_repository}/firestore-to-bq:${var.tag} || { echo "Error al subir la imagen Docker"; exit 1; }
EOT
  }
}

resource "google_cloud_run_v2_job" "firestore_to_bq" {
  depends_on = [null_resource.docker_push_bq]
  name     = "firestore-to-bigquery-job"
  location = var.region

  template {
    task_count = 1

    template {
      containers {
        image = "europe-west1-docker.pkg.dev/${var.project_id}/${var.artifact_registry_repository}/firestore-to-bq:${var.tag}"

        env {
          name  = "FIRESTORE_COLLECTION"
          value = var.firestore_collection
        }

        env {
          name  = "BIGQUERY_DATASET"
          value = var.bigquery_dataset
        }

        env {
          name  = "BIGQUERY_TABLE"
          value = var.bigquery_table
        }
      }
    }
  }
  deletion_protection = false
}

resource "null_resource" "execute_firestore-to-bq" {
  depends_on = [
    google_cloud_run_v2_job.firestore_to_bq
  ]

  provisioner "local-exec" {
    command = <<EOT
gcloud beta run jobs execute firestore-to-bigquery-job --region ${var.region} --project ${var.project_id}
EOT
  }
}

resource "google_cloud_scheduler_job" "daily_firestore_to_bq" {
  depends_on = [
    null_resource.docker_push_bq,
    google_cloud_run_v2_job.firestore_to_bq
  ]
  name     = "daily-firestore-to-bigquery-job-scheduler"
  project  = var.project_id
  region   = var.region
  schedule = "0 0 * * *"
  time_zone = "UTC"
 
  http_target {
    http_method = "POST"
    uri = "https://${var.region}-run.googleapis.com/v2/projects/${var.project_id}/locations/${var.region}/jobs/firestore-to-bigquery-job:run"
    
    # Autenticación con OAuth token desde la API
    oauth_token {
      service_account_email = google_service_account.scheduler_service_account.email
    }
  }
}

resource "google_service_account" "scheduler_service_account" {
  account_id   = "scheduler-sa"
  display_name = "Cloud Scheduler Service Account"
  project      = var.project_id
}

# Asignar el rol de invoker de Cloud Run a la cuenta de servicio
resource "google_project_iam_member" "scheduler_run_invoker" {
  depends_on = [google_service_account.scheduler_service_account]
  project = var.project_id
  role    = "roles/run.invoker"
  member  = "serviceAccount:${google_service_account.scheduler_service_account.email}"
}

resource "google_project_iam_member" "scheduler_sa_user" {
  project = var.project_id
  role    = "roles/iam.serviceAccountUser"
  member  = "serviceAccount:${google_service_account.scheduler_service_account.email}"
}