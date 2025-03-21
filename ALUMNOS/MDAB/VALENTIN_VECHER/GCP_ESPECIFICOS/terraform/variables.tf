variable "project_id" {
  description = "ID del proyecto en GCP"
  type        = string
}

variable "region" {
    description = "La región del proyecto"
    type = string 
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

variable "topic_name_environment" {
    description = "Nombre del topic para el entorno"
    type =string 
}

variable "topic_name_driving" {
    description = "Nombre del topic para el entorno"
    type =string 
}

variable "topic_name_battery" {
    description = "Nombre del topic para el entorno"
    type =string 
}

variable "city_name" {
    description = "Nombre de la ciudad donde queremos generar los datos"
    type = string 
}

variable "num_vehicle" {
    description = "Numero de vehiculos a los que queremos generar datos"
    type = number
}

variable "sub_env_name" {
    description = "Nombre de la suscripcion para el entorno"
    type = string
}

variable "sub_driv_name" {
    description = "Nombre de la suscripcion para el entorno"
    type = string
}

variable "sub_batt_name" {
    description = "Nombre de la suscripcion para el entorno"
    type = string
}

variable "artifact_repo_generator" {
    description = "Nombre del repo de artifact"
    type = string
}

variable "image_name" {
  description = "Nombre de la imagen del Pub/sub del contenedor"
  type = string 
}