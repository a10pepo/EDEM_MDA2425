variable "vpc_cidr_block" {
    type = string
    default = "10.1.0.0/16"
}

variable "availability_zones" {
  type = list(string)
  default = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]
}

variable "public_cidr_blocks" {
  type = list(string)
  default = ["10.1.1.0/24", "10.1.2.0/24", "10.1.3.0/24"]
}

variable "private_cidr_blocks" {
  type = list(string)
  default = ["10.1.11.0/24", "10.1.12.0/24", "10.1.13.0/24"]
}