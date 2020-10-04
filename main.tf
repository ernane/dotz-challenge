terraform {
  required_version = "~> 0.12.0"

  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "dotz-challenge"

    workspaces {
      name = "dotz"
    }
  }
}

provider "aws" {
  version = "~> 3.0"
  region  = var.region
}