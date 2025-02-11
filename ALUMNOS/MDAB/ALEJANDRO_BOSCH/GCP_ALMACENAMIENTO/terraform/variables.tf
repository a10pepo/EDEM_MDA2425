variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region"
  type        = string
  default     = "europe-west1"
}

variable "zone" {
  description = "The GCP zone"
  type        = string
  default     = "europe-west1-b"
}

variable "subnetwork" {
  description = "The subnetwork for the instances"
  type        = string
}

variable "service_account_email" {
  description = "Email of the service account to attach to the VMs"
  type        = string
}
