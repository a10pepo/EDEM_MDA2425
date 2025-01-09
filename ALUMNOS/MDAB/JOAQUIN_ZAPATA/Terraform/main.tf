resource "local_file" "pet" {
    filename = var.filename
    content = var.content
}
resource "local_file" "dog" {
    filename = var.filename_dog
    content = var.content_dog
}
resource "local_file" "cat" {
    filename = var.filename_cat
    content = var.content_cat
}
resource "random_pet" "my-pet" {
    prefix = var.prefix[2]
    separator = var.separator
    length = var.length
}
resource "random_pet" "my-dog" {
    prefix = var.prefix[2]
    separator = var.separator
    length = var.length
}
resource "random_pet" "my-cat" {
    prefix = var.prefix[2]
    separator = var.separator
    length = var.length
}