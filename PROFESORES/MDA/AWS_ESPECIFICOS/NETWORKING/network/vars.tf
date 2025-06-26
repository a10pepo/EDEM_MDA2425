variable "vpc_cidr_block" {
    type = string
}

variable "availability_zones" {
  type = list(string)
}

variable "public_cidr_blocks" {
  type = list(string)
}

variable "private_cidr_blocks" {
  type = list(string)
}