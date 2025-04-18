// provide an input variable for the image name
variable "image" {
  description = "The image name to use for the instance"
  type        = string
}

// create variable boolean https
variable "https" {
  description = "Enable https"
  type        = bool
  default     = false
}