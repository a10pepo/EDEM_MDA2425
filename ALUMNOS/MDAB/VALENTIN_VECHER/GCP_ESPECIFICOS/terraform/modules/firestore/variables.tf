variable "project_id" {
  description = "The ID of the project in which to create the Firestore database."
  type        = string
}
variable "firestore_db_name" {
  description = "The name of the Firestore database."
  type        = string
}
variable "location" {
  description = "The location of the Firestore database."
  type        = string
}