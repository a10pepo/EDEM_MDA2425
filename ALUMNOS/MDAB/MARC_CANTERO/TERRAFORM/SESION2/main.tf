resource "local_file" "pet" {
    filename = var.filename_pet[count.index]
    content = "My favorite pet is ${random_pet.my-pet.id}"
    count = length(var.filename_pet)
}
resource "random_pet""my-pet"{
    prefix = var.prefix[1]
    separator = var.separator
    length = var.length
}
