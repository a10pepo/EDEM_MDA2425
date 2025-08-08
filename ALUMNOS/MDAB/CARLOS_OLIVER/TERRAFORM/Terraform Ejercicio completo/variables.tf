variable "github_token" {
  description = "GitHub personal access token"
  type        = string
  sensitive   = true
}


variable "repository_name" {
  description = "Name of the GitHub repository"
  type        = string
  default     = "my-tf-repo"
}

variable "repository_owner" {
  description = "Owner of the GitHub repository"
  type        = string
  default     = "Carlos-Oliver-O"
}