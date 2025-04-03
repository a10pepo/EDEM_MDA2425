#! este es el primer cloud run que crea el job para emitir datos con pub sub
resource "null_resource" "build_and_push_docker" {

    provisioner "local-exec" {
      working_dir = path.module
      command = <<-EOT
        docker build --platform=linux/amd64 -t ${var.generator_path_to_image}
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

#! este es el segundo job que lo que hace es... 
