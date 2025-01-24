variable "filename" {
  description = "Nombre del archivo donde se guardará el contenido"
  default = [
    "pets.txt",
    "dogs.txt",
    "cats.txt",
    "turtles.txt"
  ]
}

variable "prefix" {
  description = "Prefijo que se usará para generar el nombre de la mascota"
  type        = string
  default     = "pet" 
}

variable "separator" {
  description = "Separador entre el prefijo y el nombre generado"
  type        = string
  default     = "-" 
}

variable "length" {
  description = "Longitud del nombre generado"
  type        = number
  default     = 2 
}
