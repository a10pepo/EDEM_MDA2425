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

resource "google_pubsub_subscription" "battery_sub" {
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
        docker build --platform=linux/amd64 -t ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_generator}/${var.image_name}:latest .
        docker tag ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_generator}/${var.image_name}:latest ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_generator}/${var.image_name}:latest
        docker push ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_generator}/${var.image_name}:latest
     EOT
    }
}

resource "google_cloud_run_v2_job" "default" {
  name     = var.cloud_run_job_generator_name
  depends_on = [null_resource.build_and_push_docker]
  location = var.region
  project = var.project_id

  labels = {
    environment = "production"
    team        = "data-engineering"
    component   = "generator"
  }

  template {
    template {
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_generator}/${var.image_name}"
        
        env  {
            name = "PROJECT_ID"
            value = var.project_id
        }
        env  {
            name = "TELEMETRY_BATTERY_TOPIC"
            value = var.topic_name_environment
        }
        env  {
            name = "TELEMETRY_DRIVING_TOPIC"
            value = var.topic_name_driving
        }
        env  {
            name = "TELEMETRY_ENVIRONMENT_TOPIC"
            value = var.topic_name_battery
        }
        env  {
            name = "CITY_NAME"
            value = var.city_name
        }
        env  {
            name = "NUM_VEHICLES"
            value = var.num_vehicles
        }
        }
      }
    }
}
