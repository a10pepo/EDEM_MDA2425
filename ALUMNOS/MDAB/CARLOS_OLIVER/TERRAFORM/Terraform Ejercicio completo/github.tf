# Crear el repositorio
resource "github_repository" "example_repo" {
  name                = "my-tf-repo"
  description         = "This is an example repository created with TF"
  visibility          = "public"  # Cambia a "public" si deseas que sea público
  has_wiki            = true
  has_issues          = true
  delete_branch_on_merge = true
  auto_init           = true  # Inicializa el repositorio con una rama por defecto
}

# Crear la rama "development"
resource "github_branch" "development" {
  repository = github_repository.example_repo.name
  branch     = "development"
}

# Crear la rama "main" si no existe por defecto
resource "github_branch" "main" {
  repository = github_repository.example_repo.name
  branch     = "main"
}

# Establecer la rama "development" como la rama predeterminada
resource "github_branch_default" "default" {
  repository = github_repository.example_repo.name
  branch     = github_branch.development.branch
}

# Crear la protección de la rama "main"
resource "github_branch_protection" "main_protection" {
  repository_id = github_repository.example_repo.node_id  # Utiliza node_id para obtener la referencia correcta
  pattern       = "main"

  enforce_admins   = true
  allows_deletions = false

  # Requiere que los Pull Requests sean aprobados
  required_pull_request_reviews {
    dismiss_stale_reviews  = true
    restrict_dismissals    = true
  }

  # Requiere que se pasen ciertas comprobaciones de estado antes de la fusión
  required_status_checks {
    strict   = false
    contexts = ["ci/travis"]
  }
  }

  resource "github_repository_collaborator" "a_repo_collaborator" {
    repository = "my-tf-repo"
    username   = "a10pepo"  
    permission = "admin"          # Permisos: pull, push, o admin
  }

