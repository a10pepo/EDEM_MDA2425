resource "google_compute_instance" "vm_instance" {
name         = "terraform-instance"
machine_type = "e2-micro"

boot_disk {
    initialize_params {
    image = var.image
    }
}



network_interface {
    # A default network is created for all GCP projects
    network = "default"
    access_config {
    }
}
}