resource "github_repository" "my-tf-repo" {
  description             = "This repo is created with TF"
  name                    = "my-tf-repo"
  visibility              = "public" 
  has_issues              = true
  has_wiki                = true
  auto_init               = true 
  delete_branch_on_merge  = true
}

resource "github_branch" "main" {
  repository = github_repository.my-tf-repo.name
  branch     = "main"
}

resource "github_branch_default" "default" {
  repository = github_repository.my-tf-repo.name
  branch     = github_branch.main.branch
}

resource "github_branch" "develop" {
  repository = github_repository.my-tf-repo.name
  branch     = "develop"
}

resource "github_repository_collaborator" "a10pepo-adm" {
  username   = "a10pepo"
  repository = github_repository.my-tf-repo.name
  permission = "admin" # Permisos: "pull", "push" o "admin"
}

resource "github_actions_secret" "password" {
  repository      = github_repository.my-tf-repo.name
  secret_name     = "PASSWORD" 
  plaintext_value = "12345" 
}
