resource "google_artifact_registry_repository" "repo_generate" {
  project       = var.project_id
  location      = var.region
  repository_id = var.artifact_repo_generator
  format        = "DOCKER"
}

resource "google_artifact_registry_repository" "repo_firestore" {
  project       = var.project_id
  location      = var.region
  repository_id = var.artifact_repo_firestore_to_bq
  format        = "DOCKER"
}

resource "google_artifact_registry_repository" "repo_dataflow" {
  project       = var.project_id
  location      = var.region
  repository_id = var.artifact_repo_dataflow
  format        = "DOCKER"
}

