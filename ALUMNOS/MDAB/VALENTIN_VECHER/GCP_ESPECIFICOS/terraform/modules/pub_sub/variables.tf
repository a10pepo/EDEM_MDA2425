variable "project_id" {
    description = "ID del proyecto de GCP"
    type = string
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
