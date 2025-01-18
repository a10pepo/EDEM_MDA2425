terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.16.0"
    }
  }
}

provider "google" {
  project = "steam-circlet-447114-h5"
  region = "europe-southwest1"
}