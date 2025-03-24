variable "project" {
  description = "ID del proyecto de GCP"
  type        = string
}

variable "location" {
  description = "Región para el dataset de BigQuery"
  type        = string
}

variable "dataset_id" {
  description = "ID del dataset en BigQuery"
  type        = string
  default = "vehicle_data"
}

variable "table_id" {
  description = "ID de la tabla en BigQuery"
  type        = string
}

variable "schema_file" {
  description = "Ruta al archivo JSON que contiene el esquema"
  type        = string
  default = "modules/schemas/schema.json"
}