terraform {
  backend "s3" {
    bucket = "pnieto-tf-state"
    key    = "terraform/state-networking"
    region = "eu-central-1"  # Change to your desired AWS region
  }
}

module "network" {
  source = "./network"

    vpc_cidr_block = var.vpc_cidr_block
    availability_zones = var.availability_zones
    public_cidr_blocks = var.public_cidr_blocks
    private_cidr_blocks = var.private_cidr_blocks


  providers = {
    aws.master_region = aws.master_region
  }

}