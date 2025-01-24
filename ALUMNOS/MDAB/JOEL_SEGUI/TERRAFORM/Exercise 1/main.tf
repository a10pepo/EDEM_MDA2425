resource "local_file" "animals" {
    filename = var.filename[0]
    content = var.content[0]
}

resource "local_file" "pets" {
    filename = var.filename[1]
    content = var.content[1]
}

resource "local_file" "cats" {
    filename = var.filename[2]
    content = var.content[2]
}