variable "machine_name" {
    default = "my-first-instance-terraform-macata"
    type = string
    description = "name of my instance"
}
variable "machine_type" {
    default = "e2-micro"
    type = string
    description = "type of my instance"
}
variable "machine_zone" {
    default = "europe-southwest1-a"
    type = string
    description = "zone of my instance"
}
variable "disk_image" {
    default = "projects/debian-cloud/global/images/debian-12-bookworm-v20241210"
    type = string
    description = "image of my disk"
}
variable "topic_name" {
    default = "topic1"
}