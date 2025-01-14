resource "local_file" "animals" {
    filename = var.filename[0]
    content = var.file-content["pets"]
}

resource "local_file" "pets" {
    filename = var.filename[1]
    content = var.file-content["dogs"]
}

resource "local_file" "cats" {
    filename = var.filename[2]
    content = var.file-content["cats"]
}


resource "local_file" "pet"{
    filename = var.filename
    content = "My favourite pet is ${random_pet.my-pet.id}"
}

resource "random_pet" "my-pet"{
    prefix =  var.prefix
    separator = var.separator
    length = var.length

}