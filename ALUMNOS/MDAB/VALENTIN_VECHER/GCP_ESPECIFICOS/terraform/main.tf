module "pubsub" {
  source                       = "./modules/pub_sub"
  project_id                   = var.project_id
  topic_name_environment       = var.topic_name_environment
  topic_name_driving           = var.topic_name_driving
  topic_name_battery           = var.topic_name_battery
  sub_env_name                 = var.sub_env_name
  sub_driv_name                = var.sub_driv_name
  sub_batt_name                = var.sub_batt_name

}

module "artifact_registry" {
  source = "./modules/artifact_registry"
  project_id = var.project_id
  region = var.region
  artifact_repo_generator = var.artifact_repo_generator
  depends_on = [module.pubsub]
}

module "cloud_run_job"{
  source = "./modules/cloud_run_job"
  depends_on = [module.artifact_registry]
  #! primero ponemos el primer job que vamos a hacer
  generator_path_to_image = var.generator_path_to_image
  project_id = var.project_id
  region = var.region
  topic_name_environment = var.topic_name_environment
  topic_name_driving = var.topic_name_driving
  topic_name_battery = var.topic_name_battery
  city_name = var.city_name
  num_vehicles = var.num_vehicles
  artifact_repo_generator = var.artifact_repo_generator
  image_name = var.image_name
  cloud_run_job_generator_name = var.cloud_run_job_generator_name

  #! este es el segundo job que vamos a hacer
  
}
