resource "local_file" "pet" {
    filename = each.value
    content = "My favorite pet is ${random_pet.my-pet.id}"
    for_each = toset(var.filename)

}

resource "random_pet" "my-pet" { 
    prefix = var.prefix["1"]
    separator = var.separator 
    length = var.length
}

output "pets" {
    sensitive = true
    value = local_file.pet
}

