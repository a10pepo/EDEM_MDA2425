terraform {
  backend "s3" {
    bucket = "pnieto-tf-state"
    key    = "terraform/state-cdn"
    region = "eu-central-1"  # Change to your desired AWS region
  }
}

module "cloudfront" {
  source = "./cloudfront"
  s3_name = var.s3_name
}