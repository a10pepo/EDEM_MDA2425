resource "google_firestore_database" "database" {
  project     = var.project_id
  name        = var.firestore_db_name
  location_id = var.location
  type        = "DATASTORE_MODE"
}