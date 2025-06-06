terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.24.0"
    }
  }
}

provider "google" {
    project = var.project_id
    region = var.region
    zone = var.zone
}

provider "google-beta" {
  project = var.project_id
  region  = var.region
  zone = var.zone
 
}