resource "github_repository" "example" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = var.repository_visibility
}

resource "github_branch" "main" {
  repository = github_repository.example.name
  branch     = "main"
}
