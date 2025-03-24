output "cloud_run_job_name" {
  description = "El nombre del Cloud Run Job desplegado (v2)"
  value       = google_cloud_run_v2_job.vehicle_data_job.name
}

