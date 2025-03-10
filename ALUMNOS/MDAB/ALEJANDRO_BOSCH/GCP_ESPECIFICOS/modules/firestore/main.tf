resource "google_firestore_database" "database" {
  project     = var.project
  name        = var.name
  location_id = var.location_id
  type        = var.type
  deletion_policy = "DELETE"
}