# Define project ID (best practice)
variable "project_id" {
  type        = string
  description = "The GCP project ID"
  default     = "smooth-bond-447114-p2" # Replace with your project ID
}

# Create Pub/Sub topic 1
resource "google_pubsub_topic" "topic1" {
  name    = "my-terraform-topic-1"
  project = var.project_id
}

# Create Pub/Sub topic 2
resource "google_pubsub_topic" "topic2" {
  name    = "my-terraform-topic-2"
  project = var.project_id
}

# Create Pub/Sub subscription 1 for topic 1
resource "google_pubsub_subscription" "subscription1" {
  name  = "my-terraform-subscription-1"
  topic = google_pubsub_topic.topic1.name
  project = var.project_id
}

# Create Pub/Sub subscription 2 for topic 2
resource "google_pubsub_subscription" "subscription2" {
  name  = "my-terraform-subscription-2"
  topic = google_pubsub_topic.topic2.name
  project = var.project_id

}

# Output the topic and subscription names
output "topic1_name" {
  value = google_pubsub_topic.topic1.name
}

output "topic2_name" {
  value = google_pubsub_topic.topic2.name
}

output "subscription1_name" {
  value = google_pubsub_subscription.subscription1.name
}

output "subscription2_name" {
  value = google_pubsub_subscription.subscription2.name
}