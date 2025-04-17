resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.dataset_id
  project    = var.project
  location   = var.location
}

resource "google_bigquery_table" "table" {
  dataset_id = google_bigquery_dataset.dataset.dataset_id
  table_id   = var.table_id
  schema     = file(var.schema_file)
  project    = var.project
  deletion_protection=false
}