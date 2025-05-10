terraform {
    backend "gcs" {
        bucket = "terraform_state_macata"
        prefix = "terraform/state"
    }
}

module "server1" {
  disk_image = "projects/debian-cloud/global/images/debian-12-bookworm-v20241210"
  source = "./server"
}

module "server2" {
  disk_image = 
  source = "./server"
}