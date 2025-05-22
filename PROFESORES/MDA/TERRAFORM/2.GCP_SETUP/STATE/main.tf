terraform {
  backend "gcs" {
    bucket  = "pnieto_terraform_state"
    prefix  = "terraform/state"
  }
}

resource "google_storage_bucket" "sample-element-pnieto" {
  name = "sample-element-pnieto"
  location = "europe-west1"
  storage_class = "STANDARD"
  force_destroy = true
}