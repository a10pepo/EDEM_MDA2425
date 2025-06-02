module "artifact_registry" {
  source = "./modules/artifact_registry"
  repository_id = var.repository_id
  location = var.region
  format = "DOCKER"
  description = "Repositorio para imágenes Docker"
  }


module "pubsub_enviroment" {
  source            = "./modules/pubsub"
  topic_name        = "enviroment-events"
  subscription_name = "enviroment-events-sub"
}

module "pubsub_battery" {
  source            = "./modules/pubsub"
  topic_name        = "battery-events"
  subscription_name = "battery-events-sub"
}

module "pubsub_driving" {
  source            = "./modules/pubsub"
  topic_name        = "driving-events"
  subscription_name = "driving-events-sub"
}

module "pubsub_critical_battery" {
  source            = "./modules/pubsub"
  topic_name        = "critical-battery-events"
  subscription_name = "critical-battery-sub"
}

module "firestore" {
  source = "./modules/firestore"
  project = var.project_id
}

module "bigquery" {
  source = "./modules/bigquery"
  project = var.project_id
  location = var.region
  table_id = "analytical-database"
}

module "cloud_function" {
  source         = "./modules/cloud_function"
  project_id     = var.project_id
  region         = var.region
  repository_id  = var.repository_id
  image_name     = var.cloud_image_name
  tag            = var.cloud_tag
  pubsub_topic   = "projects/${var.project_id}/topics/${module.pubsub_critical_battery.topic_name}"
  depends_on = [ module.artifact_registry ]
}

module "grafana" {
  source = "./modules/cloud_run_service"
  region = var.region
  
}

module "dataflow" {
  source = "./modules/dataflow"
  
  project_id                         = var.project_id
  build_context_dir = "C:/EDEM_MDA2425/ALUMNOS/MDAB/ALEJANDRO_BOSCH/GCP_ESPECIFICOS/dataflow"
  location                           = var.region
  region                             = var.region
  artifact_repo_id                   = module.artifact_registry.repository_id
  battery_telemetry_subscription     = "projects/${var.project_id}/subscriptions/${module.pubsub_battery.subscription_name}"
  driving_telemetry_subscription     = "projects/${var.project_id}/subscriptions/${module.pubsub_driving.subscription_name}"
  environment_telemetry_subscription = "projects/${var.project_id}/subscriptions/${module.pubsub_enviroment.subscription_name}"
  output_topic                       = "projects/${var.project_id}/topics/${module.pubsub_critical_battery.topic_name}"

  depends_on = [
    module.artifact_registry,
    module.pubsub_battery,
    module.pubsub_critical_battery,
    module.pubsub_driving,
    module.pubsub_enviroment,
    module.firestore,
    module.bigquery
  ]
}

module "cloud_run_job" {
  source = "./modules/cloud_run_job"
  depends_on = [google_service_account.scheduler, google_project_iam_member.scheduler_run_invoker, module.dataflow]
  region                      = var.region
  build_context_dir = "C:/EDEM_MDA2425/ALUMNOS/MDAB/ALEJANDRO_BOSCH/GCP_ESPECIFICOS/generators"
  build_context_dir_bq = "C:/EDEM_MDA2425/ALUMNOS/MDAB/ALEJANDRO_BOSCH/GCP_ESPECIFICOS/firestore-to-bq"
  artifact_registry_repository = module.artifact_registry.repository_id
  image_repository            = "europe-west1-docker.pkg.dev/${var.project_id}/${module.artifact_registry.repository_id}/generators"
  project_id                  = var.project_id
  telemetry_battery_topic     = module.pubsub_battery.topic_name
  telemetry_driving_topic     = module.pubsub_driving.topic_name
  telemetry_environment_topic = module.pubsub_enviroment.topic_name
  bigquery_dataset            = module.bigquery.dataset_id
  bigquery_table              = module.bigquery.table_id
  scheduler_service_account_email = google_service_account.scheduler.email
}

resource "google_service_account" "scheduler" {
  account_id   = "scheduler-service-account"
  display_name = "Service Account for Cloud Scheduler to invoke Cloud Run Jobs"
}

resource "google_project_iam_member" "scheduler_run_invoker" {
  project = var.project_id
  role    = "roles/run.invoker"
  member  = "serviceAccount:${google_service_account.scheduler.email}"
}