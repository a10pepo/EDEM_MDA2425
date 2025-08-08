variable "filename_pet" {
    default = [
        "pets.txt",
        "dogs.txt",
        "cats.txt",
        "cows.txt"
    ]
    type = list
    description = "the path of local file"
}
variable "content_pet" {
    default = {
        "pets" = "We love pets!"
        "animals" = "We love animals!"
    }
    type = map
    description = "the content of the file"
}
variable "my-pet" {
    type = object({
        name = string
        color = string
        age = number
        food = list(string)
        favorite_pet = bool
    })
    default = {
        name = "Bomba"
        color = "Brown"
        age = 3
        food = ["fish","turkey","beef"]
        favorite_pet = true
    }
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
    default = "1"
    type = number
    description = "qty of names"
}
