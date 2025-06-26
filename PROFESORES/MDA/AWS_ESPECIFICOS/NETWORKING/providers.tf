provider "aws" {
  region = "eu-west-1"

}

provider "aws" {
  alias  = "master_region"
  region = "eu-west-1"
}
