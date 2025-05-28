variable "project" {
  description = "ID del proyecto de Google Cloud donde se creará la base de datos Firestore"
  type        = string
}

variable "name" {
  description = "Nombre de la base de datos Firestore (generalmente '(default)')"
  type        = string
  default     = "(default)"
}

variable "location_id" {
    description = "Id de la localización"
    type = string
    default = "nam5"
}

variable "type" {
  description = "Tipo de la base de datos Firestore ('NATIVE' o 'DATASTORE_MODE')"
  type        = string
  default     = "FIRESTORE_NATIVE"
}