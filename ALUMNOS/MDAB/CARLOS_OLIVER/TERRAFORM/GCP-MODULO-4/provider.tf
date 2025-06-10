terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.16.0"
    }
  }
}

provider "google" {
  project     = "smooth-bond-447114-p2"
  region      = "europe-southwest1"
}
