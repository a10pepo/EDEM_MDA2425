variable "vpc_id" {
  description = "The ID of the VPC"
  type        = string
}

variable "subnet_ids" {
  description = "A list of subnet IDs within the VPC"
  type        = list(string)
}

variable "security_group_ids" {
  description = "A list of security group IDs to assign to the MSK cluster"
  type        = list(string)
}

variable "msk_cluster_name" {
  description = "The name of the MSK cluster"
  type        = string
  default     = "my-msk-cluster"
}

variable "msk_broker_instance_type" {
  description = "The instance type to use for the MSK brokers"
  type        = string
  default     = "kafka.m5.large"
}

variable "msk_number_of_broker_nodes" {
  description = "The number of broker nodes in the MSK cluster"
  type        = number
  default     = 3
}