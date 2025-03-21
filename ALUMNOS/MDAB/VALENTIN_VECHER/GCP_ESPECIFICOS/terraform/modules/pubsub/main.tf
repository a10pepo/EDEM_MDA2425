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

resource "google_pubsub_subscription" "environment_sub" {
    name = var.sub_env_name
    topic = google_pubsub_topic.topic_environment.name 
    project = var.project_id
    depends_on = [google_pubsub_topic.topic_environment] 
}


resource "google_pubsub_subscription" "driving_sub" {
    name = var.sub_driv_name
    topic = google_pubsub_topic.topic_driving.name 
    project = var.project_id 
    depends_on = [google_pubsub_topic.topic_driving]
}

resource "google_pubsub_subscription" "environment_sub" {
    name = var.sub_batt_name
    topic = google_pubsub_topic.topic_battery.name 
    project = var.project_id 
    depends_on = [google_pubsub_topic.topic_battery]
}

resource "google_artifact_registry_repository" "repo_generate" {
  project       = var.project_id
  location      = var.region
  repository_id = var.artifact_repo_generator
  format        = "DOCKER"
}

resource "null_resource" "build_and_push_docker" {
    depends_on = [ google_artifact_registry_repository.repo_generate ]

    provisioner "local-exec" {
      working_dir = path.module
      command = <<-EOT
        docker build --platform=linux/amd64 -t europe-west1-docker.pkg.dev/${var.project_id}/${var.artifact_repo_generator}/${var.image_name}:latest .
        docker push europe-west1-docker.pkg.dev/${var.project_id}/${var.artifact_repo_generator}/${var.image_name}:latest
     EOT
    }
}