resource "google_pubsub_topic" "topic_environment" {
    name = var.topic_name_environment
    project=  var.project_id
    
}

resource "google_pubsub_topic" "topic_driving" {
    name = var.topic_name_driving
    project=  var.project_id
    
}

resource "google_pubsub_topic" "topic_battery" {
    name = var.topic_name_battery
    project=  var.project_id
    
}

