terraform {
  backend "s3" {
    bucket = "pnieto-tf-state"
    key    = "terraform/state-msk"
    region = "eu-central-1"  # Change to your desired AWS region
  }
}

module "msk" {
  source = "./msk"
  vpc_id = var.vpc_id
  subnet_ids = var.subnet_ids
  security_group_ids = var.security_group_ids
  msk_cluster_name = var.msk_cluster_name
  msk_broker_instance_type = var.msk_broker_instance_type
  msk_number_of_broker_nodes = var.msk_number_of_broker_nodes

}