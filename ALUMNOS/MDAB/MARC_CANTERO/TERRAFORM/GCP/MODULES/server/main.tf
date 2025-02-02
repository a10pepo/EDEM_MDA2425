resource "google_compute_instance" "default" {
  name         = var.machine_name
  machine_type = var.machine_type
  zone         = var.machine_zone

  tags = ["http-server", "https-server"]

  boot_disk {
    initialize_params {
        size = 10
      image = var.disk_image
      labels = {
        my_label = "value"
      }
    }
  }
  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }

  metadata = {
    name = "Marc"
    subject = "TERRAFORM"
  }

  metadata_startup_script = "echo hi > /test.txt"

}
