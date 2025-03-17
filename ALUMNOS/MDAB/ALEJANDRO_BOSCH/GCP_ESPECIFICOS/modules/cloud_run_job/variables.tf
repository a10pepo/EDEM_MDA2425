variable "build_context_dir" {
  description = "Directorio de contexto para construir la imagen Docker (por ejemplo, el path donde se encuentra el Dockerfile)"
  type        = string
}

variable "build_context_dir_bq" {
  description = "Directorio de contexto para construir la imagen Docker (por ejemplo, el path donde se encuentra el Dockerfile)"
  type        = string
}

variable "project_id" {
  description = "ID del proyecto en GCP (también usado en la ruta de Artifact Registry y en los argumentos del job)"
  type        = string
}

variable "artifact_registry_repository" {
  description = "Nombre del repositorio en Artifact Registry (por ejemplo, 'my-docker-repo')"
  type        = string
}

variable "tag" {
  description = "Etiqueta que se usará para la imagen Docker (por defecto 'latest')"
  type        = string
  default     = "latest"
}

variable "region" {
  description = "Región donde se desplegará el Cloud Run Job (por ejemplo, 'europe-west1')"
  type        = string
}


variable "image_repository" {
  description = "Ruta completa del repositorio para Cloud Run."
  type        = string
}

variable "image_tag" {
  description = "Etiqueta de la imagen a utilizar en Cloud Run Job"
  type        = string
  default     = "latest"
}

variable "telemetry_battery_topic" {
  description = "Nombre del PubSub topic para la telemetría de batería"
  type        = string
}

variable "telemetry_driving_topic" {
  description = "Nombre del PubSub topic para la telemetría de conducción"
  type        = string
}

variable "telemetry_environment_topic" {
  description = "Nombre del PubSub topic para la telemetría ambiental"
  type        = string
}

variable "city_name" {
  description = "Nombre de la ciudad para la generación de datos"
  type        = string
  default = "Alcàsser"
}

variable "firestore_collection" {
  description = "Name of the Firestore collection to export data from."
  type        = string
  default = "vehicle_telemetry_data"
}

variable "bigquery_dataset" {
  description = "BigQuery dataset where the data will be loaded."
  type        = string
}

variable "bigquery_table" {
  description = "BigQuery table where the data will be loaded."
  type        = string
}

variable "scheduler_service_account_id" {
  description = "El identificador (account_id) para la cuenta de servicio de Cloud Scheduler."
  type        = string
  default     = "scheduler-service-account"
}

variable "scheduler_service_account_display_name" {
  description = "El nombre descriptivo para la cuenta de servicio de Cloud Scheduler."
  type        = string
  default     = "Service Account for Cloud Scheduler to invoke Cloud Run Jobs"
}

variable "scheduler_service_account_email" {
  description = "Email of the Cloud Scheduler service account to use for authenticating job execution."
  type        = string
}