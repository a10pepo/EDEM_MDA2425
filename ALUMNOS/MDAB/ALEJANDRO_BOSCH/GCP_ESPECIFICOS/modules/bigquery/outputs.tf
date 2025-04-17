output "dataset_id" {
  description = "ID del dataset creado"
  value       = google_bigquery_dataset.dataset.dataset_id
}

output "table_id" {
  description = "ID de la tabla creada"
  value       = google_bigquery_table.table.table_id
}