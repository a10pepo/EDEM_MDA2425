terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.16.0"
    }
  }
}

provider "google" {
  project = "copper-pixel-443112-h3"
  region = "europe-southwest1"
  zone = "europe-southwest1-a"
}