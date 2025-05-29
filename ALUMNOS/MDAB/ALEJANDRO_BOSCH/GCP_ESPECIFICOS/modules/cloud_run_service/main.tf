resource "google_cloud_run_service" "grafana" {
  name     = var.image_name_grafana
  location = var.region

  template {
    spec {
      containers {
        image = "grafana/grafana:latest"
        ports {
          container_port = 3000
        }
        env {
          name  = "GF_SECURITY_ADMIN_USER"
          value = "admin"
        }
        env {
          name  = "GF_SECURITY_ADMIN_PASSWORD"
          value = "edem_2025"
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}


resource "google_cloud_run_service_iam_member" "noauth" {
  location = google_cloud_run_service.grafana.location
  project  = google_cloud_run_service.grafana.project
  service  = google_cloud_run_service.grafana.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}



