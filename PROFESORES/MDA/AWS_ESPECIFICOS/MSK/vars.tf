variable "vpc_id" {
  description = "The ID of the VPC"
  type        = string
  default = "vpc-035b5ba6ae325c236"
}

variable "subnet_ids" {
  description = "A list of subnet IDs within the VPC"
  type        = list(string)
  default = [ "subnet-0fd358864209f8793", "subnet-08c33d26273d4c318", "subnet-0ba546ed379ef8fc6" ]
}

variable "security_group_ids" {
  description = "A list of security group IDs to assign to the MSK cluster"
  type        = list(string)
  default = [ "sg-0241c8b9a97c9a417" ]
}

variable "msk_cluster_name" {
  description = "The name of the MSK cluster"
  type        = string
  default     = "my-msk-cluster"
}

variable "msk_broker_instance_type" {
  description = "The instance type to use for the MSK brokers"
  type        = string
  default     = "kafka.t3.small"
}

variable "msk_number_of_broker_nodes" {
  description = "The number of broker nodes in the MSK cluster"
  type        = number
  default     = 3
}
