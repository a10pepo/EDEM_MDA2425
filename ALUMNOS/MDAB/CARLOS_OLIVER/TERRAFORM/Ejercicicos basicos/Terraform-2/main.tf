resource "local_file" "pet" {
    filename = var.filename
    content = var.content
}

resource "local_file" "dog" {
    filename = var.filename
    content = var.content
}

resource "local_file" "cat" {
    filename = var.filename
    content = var.content
}
