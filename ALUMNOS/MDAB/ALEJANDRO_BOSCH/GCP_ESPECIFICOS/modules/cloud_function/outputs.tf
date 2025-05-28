output "function_name" {
  description = "Nombre de la Cloud Function desplegada"
  value       = google_cloudfunctions2_function.notify-critical-battery-v2.name
}