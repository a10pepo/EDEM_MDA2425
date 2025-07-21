# DELIVERY APP VM
resource "google_compute_instance_from_machine_image" "delivery_app" {
  name           = "delivery-app"
  provider       = google-beta
  zone           = var.zone
  source_machine_image  = "projects/${var.project_id}/global/machineImages/image-template-edem"
  machine_type   = "e2-micro"

  network_interface {
    subnetwork = var.subnetwork
    access_config {
        // Ephemeral IP
    }
  }

  service_account {
    email  = var.service_account_email
    scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
      "https://www.googleapis.com/auth/sqlservice.admin",
      "https://www.googleapis.com/auth/pubsub"
    ]
  }
  allow_stopping_for_update = true 
}

# ORDERS APP VM
resource "google_compute_instance_from_machine_image" "orders_app" {
  name           = "orders-app"
  provider       = google-beta
  zone           = var.zone
  source_machine_image  = "projects/${var.project_id}/global/machineImages/image-template-edem"
  machine_type   = "e2-micro"

  network_interface {
    subnetwork = var.subnetwork
    access_config {
        // Ephemeral IP
    }
  }

  service_account {
    email  = var.service_account_email
    scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
      "https://www.googleapis.com/auth/sqlservice.admin",
      "https://www.googleapis.com/auth/pubsub"
    ]
  }

  allow_stopping_for_update = true 
}

# order_events Pub/Sub topic and subscription
resource "google_pubsub_topic" "order_events" {
  name = "order-events"
}

resource "google_pubsub_subscription" "order_events_sub" {
  name  = "${google_pubsub_topic.order_events.name}-sub"
  topic = google_pubsub_topic.order_events.name
}

# delivery_events Pub/Sub topic
resource "google_pubsub_topic" "delivery_events" {
  name = "delivery-events"
}


# Postgres SQL instance
resource "google_sql_database_instance" "postgres_instance" {
  name             = "edem-mimove-postgres"
  region           = var.region
  database_version = "POSTGRES_15"
  settings {
    tier            = "db-f1-micro" 
    availability_type = "ZONAL"
    disk_size       = 100 # GB
    # deletion_protection = false

    ip_configuration {
      ipv4_enabled = true
      authorized_networks {
        name  = "public-access"
        value = "0.0.0.0/0"
      }
    }
  }
  lifecycle {
    prevent_destroy = false
  }
}

resource "google_sql_user" "postgres_user" {
  name     = "postgres"
  instance = google_sql_database_instance.postgres_instance.name
  password = "EDEM2425"
}

resource "google_sql_database" "ecommerce" {
  name     = "ecommerce"
  instance = google_sql_database_instance.postgres_instance.name
}