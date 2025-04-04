#! este es el primer cloud run que crea el job para emitir datos con pub sub
resource "null_resource" "build_and_push_docker_gen_data" {

  provisioner "local-exec" {
    working_dir = path.module
    command     = <<-EOT
        
        
        docker build --platform=linux/amd64 -t ${var.image_name}:latest -f ${var.generator_path_to_image} $(dirname ${var.generator_path_to_image})
        
        
        docker tag ${var.image_name}:latest ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_generator}/${var.image_name}:latest
        
        
        docker push ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_generator}/${var.image_name}:latest
     
     EOT
  }
}

resource "google_cloud_run_v2_job" "generator_job" {
  name       = var.cloud_run_job_generator_name
  depends_on = [null_resource.build_and_push_docker_gen_data]
  location   = var.region
  project    = var.project_id

  labels = {
    environment = "production"
    team        = "data-engineering"
    component   = "generator"
  }

  template {
    template {
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_generator}/${var.image_name}"

        env {
          name  = "PROJECT_ID"
          value = var.project_id
        }
        env {
          name  = "TELEMETRY_BATTERY_TOPIC"
          value = var.topic_name_environment
        }
        env {
          name  = "TELEMETRY_DRIVING_TOPIC"
          value = var.topic_name_driving
        }
        env {
          name  = "TELEMETRY_ENVIRONMENT_TOPIC"
          value = var.topic_name_battery
        }
        env {
          name  = "CITY_NAME"
          value = var.city_name
        }
        env {
          name  = "NUM_VEHICLES"
          value = var.num_vehicles
        }
      }
    }
  }
}

#! este es el segundo job que lo que hace es hacer copia de los datos de firestore a bigquery

resource "null_resource" "push_docker_firestore_to_bq" {
  provisioner "local-exec" {
    working_dir = path.module
    command     = <<-EOT
      
      docker build --platform=linux/amd64 -t ${var.image_name_firestore_to_bq}:latest -f ${var.firestore_to_bq_path} $(dirname ${var.firestore_to_bq_path})
      
      
      docker tag ${var.image_name_firestore_to_bq}:latest ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_firestore_to_bq}/${var.image_name_firestore_to_bq}:latest
      
      
      docker push ${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_firestore_to_bq}/${var.image_name_firestore_to_bq}:latest
   
   EOT
  }
}

resource "google_cloud_run_v2_job" "job_fire" {
  name       = var.cloud_run_job_firestore_to_bq_name
  depends_on = [null_resource.push_docker_firestore_to_bq]
  location   = var.region
  project    = var.project_id
  labels = {
    environment = "production"
    team        = "data-engineering"
    component   = "firestore-to-bq"
  }
  template {
    template {
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.artifact_repo_firestore_to_bq}/${var.image_name_firestore_to_bq}"

        env {
          name  = "FIRESTORE_COLLECTION"
          value = var.firestore_collection
        }

        env {
          name  = "BIGQUERY_DATASET"
          value = var.bigquery_dataset
        }

        env {
          name  = "BIGQUERY_TABLE"
          value = var.bigquery_table
        }
      }
    }
  }
}