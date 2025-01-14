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

#AQUI SE PONEN TODOS LOS PROVIDERS QUE SE VAN A UTILIZAR (EN ESTE CASO, EL LOCAL YA LO USA DE BASE)