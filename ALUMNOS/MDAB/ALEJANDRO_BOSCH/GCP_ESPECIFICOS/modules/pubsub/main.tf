resource "google_pubsub_topic" "prueba" {
  name = var.topic_name
}

resource "google_pubsub_subscription" "prueba" {
  name  = var.subscription_name
  topic = google_pubsub_topic.prueba.name
}