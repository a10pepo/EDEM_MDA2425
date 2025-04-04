variable "generator_path_to_image" {
  description = "El path del docker del generador"
  type        = string
}

variable "project_id" {
  description = "ID del proyecto de GCP"
  type        = string
}

variable "region" {
  description = "La región del proyecto"
  type        = string
}

variable "topic_name_environment" {
  description = "Nombre del topic para el entorno"
  type        = string
}

variable "topic_name_driving" {
  description = "Nombre del topic para el entorno"
  type        = string
}

variable "topic_name_battery" {
  description = "Nombre del topic para el entorno"
  type        = string
}

variable "city_name" {
  description = "Nombre de la ciudad donde queremos generar los datos"
  type        = string
}

variable "num_vehicles" {
  description = "Numero de vehiculos a los que queremos generar datos"
  type        = number
}

variable "artifact_repo_generator" {
  description = "Nombre del repo de artifact"
  type        = string
}

variable "image_name" {
  description = "Nombre de la imagen del contenedor"
  type        = string
}

variable "image_name_firestore_to_bq" {
  description = "Nombre de la imagen del contenedor encargado del codigo de pasar la info de firestore a bigquery"
  type        = string
}

variable "cloud_run_job_generator_name" {
  description = "Nombre del job de cloud run"
  type        = string
}

variable "firestore_to_bq_path" {
  description = "El path del docker del firestore to bq"
  type        = string
}

variable "cloud_run_job_firestore_to_bq_name" {
  description = "Nombre del job de cloud run"
  type        = string
}
variable "firestore_collection" {
  description = "Nombre de la coleccion de firestore"
  type        = string
}

variable "bigquery_dataset" {
  description = "Nombre del dataset de bigquery"
  type        = string
}
variable "bigquery_table" {
  description = "Nombre de la tabla de bigquery"
  type        = string
}

variable "artifact_repo_firestore_to_bq" {
  description = "Nombre del repo de artifact"
  type        = string
}