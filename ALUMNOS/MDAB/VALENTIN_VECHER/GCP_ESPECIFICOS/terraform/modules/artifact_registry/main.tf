resource "google_artifact_registry_repository" "repo_generate" {
  project       = var.project_id
  location      = var.region
  repository_id = var.artifact_repo_generator
  format        = "DOCKER"
}