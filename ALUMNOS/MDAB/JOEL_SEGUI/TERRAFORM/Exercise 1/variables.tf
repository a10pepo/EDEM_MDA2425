variable "filename" {
    default = ["pets.txt","dogs.txt", "cats.txt"]
    type = list
    description = "The path of the local file"
}

variable "content" {
    default = ["I love pets","I love dogs","I love cats"]
    type = list
    description = "the content of the file"
}
