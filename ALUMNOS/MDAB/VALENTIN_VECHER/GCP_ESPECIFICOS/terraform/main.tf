terraform {
  backend "gcs"{
    bucket = "vavego-terraform-state-project-javibrio-bucket"
    prefix = "terraform/state"
  }
}


module "bucket"{
  source = "./modules/bucket"
  bucket_name_dataflow = var.bucket_name_dataflow
  location            = var.location
}

module "pubsub" {
  source                 = "./modules/pub_sub"
  project_id             = var.project_id
  topic_name_environment = var.topic_name_environment
  topic_name_driving     = var.topic_name_driving
  topic_name_battery     = var.topic_name_battery
  sub_env_name           = var.sub_env_name
  sub_driv_name          = var.sub_driv_name
  sub_batt_name          = var.sub_batt_name
  firestore_pubsub_topic = var.firestore_pubsub_topic
  firestore_pubsub_sub   = var.firestore_pubsub_sub
}

module "artifact_registry" {
  source                        = "./modules/artifact_registry"
  project_id                    = var.project_id
  region                        = var.region
  artifact_repo_generator       = var.artifact_repo_generator
  artifact_repo_firestore_to_bq = var.artifact_repo_firestore_to_bq

  depends_on = [module.pubsub]
}

module "cloud_run_job" {
  source                             = "./modules/cloud_run_job"
  depends_on                         = [module.artifact_registry]
  generator_path_to_image            = var.generator_path_to_image
  project_id                         = var.project_id
  region                             = var.region
  topic_name_environment             = var.topic_name_environment
  topic_name_driving                 = var.topic_name_driving
  topic_name_battery                 = var.topic_name_battery
  city_name                          = var.city_name
  num_vehicles                       = var.num_vehicles
  artifact_repo_generator            = var.artifact_repo_generator
  image_name                         = var.image_name
  cloud_run_job_generator_name       = var.cloud_run_job_generator_name
  firestore_to_bq_path               = var.firestore_to_bq_path
  image_name_firestore_to_bq         = var.image_name_firestore_to_bq
  firestore_collection               = var.firestore_collection
  bigquery_dataset                   = var.bigquery_dataset
  bigquery_table                     = var.bigquery_table
  cloud_run_job_firestore_to_bq_name = var.cloud_run_job_firestore_to_bq_name
  artifact_repo_firestore_to_bq      = var.artifact_repo_firestore_to_bq
}

module "firestore" {
  source = "./modules/firestore"
  project_id = var.project_id
  firestore_db_name = var.firestore_db_name
  location = var.location
} 