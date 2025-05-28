provider "aws" {
  region = "eu-west-1"
}

resource "aws_ecr_repository" "example" {
  name                 = "my-ecr-repo"
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
  tags = {
    Name = "my-ecr-repo"
  }
}