resource "google_pubsub_topic" "mi_topico" {
  name = "mi-topico"
}

resource "google_pubsub_subscription" "suscripcion_1" {
  name  = "suscripcion-1"
  topic = google_pubsub_topic.mi_topico.name  
}

resource "google_pubsub_subscription" "suscripcion_2" {
  name  = "suscripcion-2"
  topic = google_pubsub_topic.mi_topico.name  
}
