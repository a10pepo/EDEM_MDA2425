resource "google_pubsub_topic" "topic_environment" {
  name    = var.topic_name_environment
  project = var.project_id

}

resource "google_pubsub_topic" "topic_driving" {
  name    = var.topic_name_driving
  project = var.project_id

}

resource "google_pubsub_topic" "topic_battery" {
  name    = var.topic_name_battery
  project = var.project_id

}

resource "google_pubsub_subscription" "environment_sub" {
  name       = var.sub_env_name
  topic      = google_pubsub_topic.topic_environment.name
  project    = var.project_id
  depends_on = [google_pubsub_topic.topic_environment]
}


resource "google_pubsub_subscription" "driving_sub" {
  name       = var.sub_driv_name
  topic      = google_pubsub_topic.topic_driving.name
  project    = var.project_id
  depends_on = [google_pubsub_topic.topic_driving]
}

resource "google_pubsub_subscription" "battery_sub" {
  name       = var.sub_batt_name
  topic      = google_pubsub_topic.topic_battery.name
  project    = var.project_id
  depends_on = [google_pubsub_topic.topic_battery]
}