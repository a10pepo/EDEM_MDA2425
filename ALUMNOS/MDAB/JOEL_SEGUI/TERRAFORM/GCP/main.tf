terraform {
    backend "gcs" {
      bucket = "terraform_state_joel"
      prefix = "terraform/state"
    }
    
}
resource "google_compute_instance" "vm_instance" {
  name         = "my-first-instance-terraform-joelsf"
  machine_type = "e2-micro"
  zone = "europe-southwest1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }
  tags = ["http-server", "https-server"]
}