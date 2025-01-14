
resource "github_repository" "mi_repositorio" {
  name        = var.name
  description = var.description
  visibility  = var.visib
  has_issues  = var.issues
  has_wiki    = var.wiki
  delete_branch_on_merge = var.merge
  auto_init = true
}
resource "github_branch_default" "default" {
  repository = github_repository.mi_repositorio.name
  branch     = "main"
}
resource "github_branch" "develop" {
  repository = github_repository.mi_repositorio.name
  branch     = "develop"
}
resource "github_repository_collaborator" "example" {
  repository = github_repository.mi_repositorio.name
  username   = "a10pepo"
  permission = "push"
}