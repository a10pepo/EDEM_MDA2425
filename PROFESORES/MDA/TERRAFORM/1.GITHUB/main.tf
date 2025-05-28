resource "github_repository" "example" {
  name        = "example-repo"
  description = "This is an example repository created with Terraform"
  visibility  = "public"
}

resource "github_branch" "main" {
  repository = github_repository.example.name
  branch     = "main"
}

