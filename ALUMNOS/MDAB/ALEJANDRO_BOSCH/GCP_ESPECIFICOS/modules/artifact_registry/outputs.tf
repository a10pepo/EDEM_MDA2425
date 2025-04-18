output "repository_id" {
  description = "El ID del repositorio creado"
  value       = google_artifact_registry_repository.repo.repository_id
}