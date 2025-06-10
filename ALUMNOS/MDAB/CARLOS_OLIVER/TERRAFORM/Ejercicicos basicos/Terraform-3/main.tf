resource "random_pet" "my_pet" {# Puedes cambiar el prefijo según lo que necesites
  separator = "-"
  length    = 2
}

resource "local_file" "pet" {
    content = "hola"
    filename = var.filename[count.index]
    count = length(var.filename)
}