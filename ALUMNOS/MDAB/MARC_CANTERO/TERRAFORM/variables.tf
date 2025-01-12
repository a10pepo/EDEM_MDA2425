variable "filename_pet" {
    default = "pets.txt"
    type = string
    description = "the path of local file"
}
variable "content_pet" {
    default = "We love pets!"
    type = string
    description = "the content of the file"
}
variable "filename_cat" {
    default = "cats.txt"
    type = string
    description = "the path of local file"
}
variable "content_cat" {
    default = "We love cats!"
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
variable "prefix_pet" {
    default = ["Mr","Mrs","Sir"]
    type = list
    description = "the prefix to be set"
}
variable "prefix_cat" {
    default = ["Mr","Mrs","Sir"]
    type = list
    description = "the prefix to be set"
}
variable "prefix_dog" {
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
    default = "1"
    type = number
    description = "qty of names"
}
variable "password_change" {
    default = true
    type = bool
}