provider "google" {
  project = "edem-363212"
  region  = "europe-southwest1"
  zone    = "europe-southwest1-a"
}

resource "google_compute_instance" "vm_instance" {
name         = "terraform-instance"
machine_type = "e2-micro"

boot_disk {
    initialize_params {
    image = "debian-cloud/debian-11"
    }
}



network_interface {
    # A default network is created for all GCP projects
    network = "default"
    access_config {
    }
}
}

resource "google_storage_bucket" "pnieto" {
  location = "EU"
  name     = "pnieto-bucket"
}