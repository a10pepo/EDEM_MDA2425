variable "project_id" {
  description = "ID del proyecto en GCP"
  type        = string
}

variable "region" {
  description = "Región de despliegue en GCP"
  type        = string
  default     = "europe-west1"
}

variable "zone" {
  description = "Zona de despliegue en GCP (por ejemplo, europe-west1-b)"
  type        = string
}

variable "repository_id" {
  description = "El ID del repositorio en Artifact Registry"
  type = string
}

variable "cloud_image_name" {
  description = "Nombre de la imagen Docker para la función de Cloud Functions"
  type        = string
}

variable "cloud_tag" {
  description = "Etiqueta de la imagen Docker para la función de Cloud Functions"
  type        = string
}