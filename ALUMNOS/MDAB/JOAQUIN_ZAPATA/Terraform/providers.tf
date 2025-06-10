terraform {
  required_providers {
    random = {
      source = "hashicorp/random"
      version = "3.6.3"
    }
        local = {
      source = "hashicorp/local"
      version = "2.5.2"
        }
  }
}

provider "random" {
  # Configuration options
}