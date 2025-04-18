output "url" {
  value = google_cloud_run_service.grafana.status[0].url
}

output "name" {
  value = google_cloud_run_service.grafana.name
}

output "region" {
  value = google_cloud_run_service.grafana.location
}