terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.14.1"
    }
  }
}

provider "google" {
  project = "edem-363212"
  region  = "europe-southwest1"
  zone    = "europe-southwest1-a"
}