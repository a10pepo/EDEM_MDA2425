provider "github" {
  token = var.github_token
}

resource "github_repository" "example" {
  name        = "example-repo"
  description = "This is an example repository created with Terraform"
  visibility  = "public"
}
