output "topic_id" {
  value = google_pubsub_topic.prueba.name
}

output "subscription_id" {
  value = google_pubsub_subscription.prueba.name
}

output "topic_name" {
  description = "Nombre del tópico de Pub/Sub"
  value       = google_pubsub_topic.prueba.name
}

output "subscription_name" {
  description = "Nombre de la suscripción de Pub/Sub"
  value       = google_pubsub_subscription.prueba.name
}