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