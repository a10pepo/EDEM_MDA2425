# variable "filename" {
#     default = ["pets.txt","dogs.txt", "cats.txt"]
#     type = list(string)
#     description = "The path of the local file"
# }

variable "filename"{

}

variable file-content{
    type = map(string)
    default = {
        "pets" = "I love pets"
        "dogs" = "I love dogs"
        "cats" = "I love cats"
    }
}

variable my-pet {
    type = object({
        name = string
        color = string
        age = string
        food = list(string)
        favourite_pet = bool
    })

    default = {
        name = "Ares"
        color = "black"
        age = 15
        food = ["fish", "chicken", "eggs"]
        favourite_pet = true

    }
}