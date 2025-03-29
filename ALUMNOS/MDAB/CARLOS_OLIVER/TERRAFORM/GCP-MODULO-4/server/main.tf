
resource "google_compute_instance" "default" {
  name         = "terraform-instance-carlos"
  machine_type = "e2-micro"
  zone         = "europe-southwest1-b"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    subnetwork = "default"
    access_config { # This is essential for a public IP
      # You can leave this empty for an ephemeral IP
    }
  }

  tags = ["http-server", "https-server"] # Add a tag to link with the firewall rule
}

resource "google_storage_bucket" "coliver" {
  
}
