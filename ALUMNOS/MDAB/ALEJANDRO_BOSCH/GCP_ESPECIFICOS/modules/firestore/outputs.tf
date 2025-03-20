output "firestore_database_name" {
  description = "Nombre del recurso Firestore creado."
  value       = google_firestore_database.database.name
}