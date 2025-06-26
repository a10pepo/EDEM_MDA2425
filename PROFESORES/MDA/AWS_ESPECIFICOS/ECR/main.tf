terraform {
  backend "s3" {
    bucket = "pnieto-tf-state"
    key    = "terraform/state-ecr"
    region = "eu-central-1"  # Change to your desired AWS region
  }
}

module "ecr" {
  source = "./ecr"
  ecr_name = var.ecr_name
}