resource "local_file" "pet" {
    filename = var.filename_pet
    content = var.content_pet
}
resource "local_file" "cat" {
    filename = var.filename_cat
    content = var.content_cat
}
resource "local_file" "dog" {
    filename = var.filename_dog
    content = var.content_dog
}

resource "random_pet" "my-pet" {
    prefix = var.prefix_pet[0]
    separator = var.separator
    length = var.length
}
resource "random_pet" "my-cat" {
    prefix = var.prefix_cat[1]
    separator = var.separator
    length = var.length
}
resource "random_pet" "my-dog" {
    prefix = var.prefix_dog[2]
    separator = var.separator
    length = var.length
}