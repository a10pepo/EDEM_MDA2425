resource "google_storage_bucket" "storage_joel1091" {
}

terraform {
    backend "gcs" {
      bucket = "terraform_state_joel"
      prefix = "terraform/state"
    }
    
}

module "server1" {
    source = "./server"
    image = "ubuntu-os-cloud/ubuntu-2004-lts"
}
