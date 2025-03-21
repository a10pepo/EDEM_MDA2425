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

variable "city_name" {
    description = "Nombre de la ciudad donde queremos generar los datos"
    type = string 
}

variable "num_vehicle" {
    description = "Numero de vehiculos a los que queremos generar datos"
    type = number
}
