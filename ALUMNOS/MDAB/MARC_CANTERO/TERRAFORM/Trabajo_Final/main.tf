resource "google_compute_instance" "default" {
  name         = var.machine_name
  machine_type = var.machine_type
  zone         = var.machine_zone

  tags = ["http-server", "https-server"]

  boot_disk {
    initialize_params {
        size = 10
      image = var.disk_image
      labels = {
        my_label = "value"
      }
    }
  }
  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }

  metadata = {
    name = "Marc"
    subject = "TERRAFORM"
  }

  metadata_startup_script = "echo hi > /test.txt"
}
resource "google_pubsub_topic" "example" {
  name = var.topic_name
}
resource "google_pubsub_subscription" "example1" {
  name  = "example-subscription1"
  topic = google_pubsub_topic.example.name
}
resource "google_pubsub_subscription" "example2" {
  name  = "example-subscription2"
  topic = google_pubsub_topic.example.name
}
resource "google_pubsub_schema" "example" {
  name = "example-schema"
  type = "AVRO"
  definition = "{\n  \"type\" : \"record\",\n  \"name\" : \"Avro\",\n  \"fields\" : [\n    {\n      \"name\" : \"StringField\",\n      \"type\" : \"string\"\n    },\n    {\n      \"name\" : \"IntField\",\n      \"type\" : \"int\"\n    }\n  ]\n}\n"
}