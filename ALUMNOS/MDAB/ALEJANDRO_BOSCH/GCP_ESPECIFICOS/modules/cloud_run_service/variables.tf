variable "image_name_grafana" {
  description = "Nombre del servicio de Cloud Run para Grafana"
  type        = string
  default = "grafana"
}

variable "region" {
  description = "Región de GCP donde se desplegará el servicio"
  type        = string

}
