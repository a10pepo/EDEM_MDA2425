variable "filename" {
    default = "pets.txt"
    type = string
    description = "It's the path"
}
variable "content" {
    default = ["My favorite pet is Mrs. Whiskers",]
    type = string
    description = "the content"
}
variable "prefix" {
    default = ["Mr", "Mrs", "Sir"]
    type = list
}
variable "separator" {
    default = "."
    type = string
    description = "Separator"
}
variable "length" {
    default = "1"
    type = number
    description = "number"
}