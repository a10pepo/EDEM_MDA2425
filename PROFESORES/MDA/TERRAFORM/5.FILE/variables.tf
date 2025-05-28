variable "filename" {
    default = [
        "fish.txt"
    ]
    type = list(string)
    description = "the path of local file"
}
variable "content" { 
    default = "I love pets!"
    type = string
    description = "the content of the file"
}
variable "prefix" {
    default = ["Mr", "Mrs", "Sir"] 
    type = list(string)
}


variable "separator" {
    default = "."
}

variable "length" { 
    default = "2" 
    type = number
    description = "length of the pet name"
}

variable "password_change" {
    default = "true"
    type = bool
}

