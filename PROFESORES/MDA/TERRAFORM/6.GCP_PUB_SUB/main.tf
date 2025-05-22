resource "google_pubsub_topic" "topic" {
  name = "sample-topic"

  labels = {
    foo = "bar"
  }

  message_retention_duration = "86600s"
}