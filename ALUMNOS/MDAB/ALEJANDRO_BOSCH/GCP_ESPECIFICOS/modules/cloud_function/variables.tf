variable "project_id" {
  description = "ID del proyecto de GCP"
  type        = string
}

variable "region" {
  description = "Región de despliegue"
  type        = string
}

variable "repository_id" {
  description = "ID del repositorio en Artifact Registry"
  type        = string
}

variable "image_name" {
  description = "Nombre de la imagen Docker para la función de Discord"
  type        = string
}

variable "tag" {
  description = "Etiqueta de la imagen Docker"
  type        = string
}

variable "pubsub_topic" {
  description = "Nombre completo del tópico de Pub/Sub para el trigger (por ejemplo, 'projects/mi-proyecto/topics/matched-events')"
  type        = string
}

variable "entry_point" {
  description = "Punto de entrada de la función (debe coincidir con lo definido en main.py)"
  type        = string
  default     = "get_pubsub_message"
}

variable "artifact_registry_domain" {
  description = "Dominio de Artifact Registry según la región (ej: europe-west1-docker.pkg.dev)"
  type        = string
  default     = "europe-west1-docker.pkg.dev"
}