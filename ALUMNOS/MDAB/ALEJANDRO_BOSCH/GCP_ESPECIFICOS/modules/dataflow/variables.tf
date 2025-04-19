

variable "project_id" {
  description = "ID del proyecto GCP."
  type        = string
}

variable "region" {
  description = "Región donde se desplegará Dataflow."
  type        = string
  default     = "us-central1"
}

variable "bucket_name" {
  description = "Nombre del bucket para alojar la Flex Template."
  type        = string
  default = "alboce-dataflow-bucket"
}

variable "location" {
  description = "Ubicación (región o multi-regional) para el bucket."
  type        = string
}

variable "dataflow_job_name" {
  description = "Nombre del job de Dataflow."
  type        = string
  default = "vehicle-dataflow"
}

variable "artifact_repo_id" {
  description = "ID del repositorio en Artifact Registry donde se alojará la imagen Docker."
  type        = string
}

variable "battery_telemetry_subscription" {
  description = "PubSub subscription para los datos de batería."
  type        = string
}

variable "driving_telemetry_subscription" {
  description = "PubSub subscription para los datos de conducción."
  type        = string
}

variable "environment_telemetry_subscription" {
  description = "PubSub subscription para los datos ambientales."
  type        = string
}

variable "firestore_collection" {
  description = "Nombre de la colección en Firestore para almacenar los datos."
  type        = string
  default     = "vehicle_telemetry_data"
}

variable "output_topic" {
  description = "PubSub topic para enviar notificaciones."
  type        = string
}

variable "image_api" {
  description = "URL de la API que devuelve imágenes de tráfico."
  type        = string
  default     = "https://europe-southwest1-serverless-edem.cloudfunctions.net/getTrafficImages"
}

variable "build_context_dir" {
  description = "Directorio de contexto para construir la imagen Docker (por ejemplo, el path donde se encuentra el Dockerfile)"
  type        = string
}


