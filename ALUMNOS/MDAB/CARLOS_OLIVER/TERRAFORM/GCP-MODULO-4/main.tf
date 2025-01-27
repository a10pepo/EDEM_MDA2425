terraform {
    backend "gcs" {
        bucket = "terraform-coliver"
        prefix = "terraform/state"
    }
}

module "server" {
  source = "./server"
  image = "debian-cloud/debian-11"
}

module "server2" {
  source = "./server"
  image = "ubuntu-os.cloud/ubuntu-2004-lts"
}

