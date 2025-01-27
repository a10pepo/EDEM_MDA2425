variable "prefix" {
  description = "Prefix for the random pet name"
  type        = string
  default     = "Mrs"
}

variable "separator" {
  description = "Separator for the random pet name"
  type        = string
  default     = "-"
}

variable "length" {
  description = "Length of the random pet name"
  type        = number
  default     = 1
}

variable "filename" {
    type=list(string)
    default = [
        "pets.txt",
        "dogs.txt",
        "cats.txt",
        "rabits.txt"
    ]
}