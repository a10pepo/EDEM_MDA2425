variable "filename" {
    default = "pets.txt"
    type = string
    description = "the path of local file"
}
variable "content" {
    default = "We love pets!"
    type = string
    description = "the content of the file"
}
variable "filename_dog" {
    default = "dogs.txt"
    type = string
    description = "the path of local file"
}
variable "content_dog" {
    default = "We love dogs!"
    type = string
    description = "the content of the file"
}
variable "filename_cat" {
    default = "cat.txt"
    type = string
    description = "the path of local file"
}
variable "content_cat" {
    default = "We love cats!"
    type = string
    description = "the content of the file"
}
variable "prefix" {
    default = ["Mrs", "Mr", "Sir"]
    type = list
}
variable "separator" {
    default = "."
    type = string
    description = "separator to use"
}
variable "length" {
    default = 4
    type = number
    description = "length of the pet names"
}

variable "password_change"{
    default = true
    type = bool
}