
module repository1 {
  source = "./repository"

  repository_name = "example-repo1"
  repository_description = "This is an example repository created with Terraform"
  repository_visibility = "public"
}

module repository2 {
  source = "./repository"

  repository_name = "example-repo2"
  repository_description = "This is an example repository created with Terraform"
  repository_visibility = "public"
}






















terraform {
  backend "gcs" {
    bucket  = "pnieto_terraform_state"
    prefix  = "terraform/state"
    
  }
}


module "server" {
  source = "./server"
  image = "debian-cloud/debian-11"
  https = true

}

module "server2" {
  source = "./server"
  image = "ubuntu-os-cloud/ubuntu-2004-lts"

}