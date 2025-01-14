variable "filename" {
    default = "pets.txt"
    type = string
    description = "The path of the local file"
}

variable "content" {
    default = "My favourite pet is Mrs. Whiskers"
    type = string
    description = "the content of the file"
}

variable "prefix" {
    default = ["Mr","Mrs","Sir"]
    type = list
    description = "the prefix to be set"

}

variable "separator" {
    default = "."
    type = string
    description = "separator to use"

}

variable "length" {
    default = 2
    type = number
    description = "num lenght of the name pet"

}

variable "password_change" {
    default = true
    type = bool
  
}