# Terraform

## Iniciando o `terraform` com o backend remoto [terraform.io](https://app.terraform.io/)

```bash
terraform init
```

O comando irá construir a `workspace` para gerenciar as execuções dos `scripts terraform`

![terraform-init](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/terraform-init.png)

## Executando o plano de execução

```bash
terraform plan
```

A saída desse comando, deverá produzir uma saída parecida como essa:

```bash
Running plan in the remote backend. Output will stream here. Pressing Ctrl-C
will stop streaming the logs, but will not stop the plan running remotely.

Preparing the remote plan...

To view this run in a browser, visit:
https://app.terraform.io/app/dotz-challenge/dotz/runs/run-tE3CkaMgv8ibw3BQ

Waiting for the plan to start...

Terraform v0.12.29
Configuring remote state backend...
Initializing Terraform configuration...
2020/10/01 01:27:55 [DEBUG] Using modified User-Agent: Terraform/0.12.29 TFC/abf1fa3fed
Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be
persisted to local or remote state storage.


------------------------------------------------------------------------

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_s3_bucket.dotz_input will be created
  + resource "aws_s3_bucket" "dotz_input" {
      + acceleration_status         = (known after apply)
      + acl                         = "private"
      + arn                         = (known after apply)
      + bucket                      = "dotz-input"
      + bucket_domain_name          = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      + id                          = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      + tags                        = {
          + "Author"      = "ernane.sena@gmail.com"
          + "Environment" = "development"
          + "Project"     = "Dotz Challenge"
          + "Team"        = "dotz"
        }
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      + versioning {
          + enabled    = (known after apply)
          + mfa_delete = (known after apply)
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.
```

## Aplicando as modificações com o `terraform`

```bash
terraform apply -auto-approve
```

A saída desse comando, deverá produzir uma saída parecida como essa:

```bash
Running apply in the remote backend. Output will stream here. Pressing Ctrl-C
will cancel the remote apply if it's still pending. If the apply started it
will stop streaming the logs, but will not stop the apply running remotely.

Preparing the remote apply...

To view this run in a browser, visit:
https://app.terraform.io/app/dotz-challenge/dotz/runs/run-tyLk7LT7w7Zyk3X7

Waiting for the plan to start...

Terraform v0.12.29
Configuring remote state backend...
Initializing Terraform configuration...
2020/10/01 01:33:11 [DEBUG] Using modified User-Agent: Terraform/0.12.29 TFC/abf1fa3fed
Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be
persisted to local or remote state storage.


------------------------------------------------------------------------

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_s3_bucket.dotz_input will be created
  + resource "aws_s3_bucket" "dotz_input" {
      + acceleration_status         = (known after apply)
      + acl                         = "private"
      + arn                         = (known after apply)
      + bucket                      = "dotz-input"
      + bucket_domain_name          = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      + id                          = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      + tags                        = {
          + "Author"      = "ernane.sena@gmail.com"
          + "Environment" = "development"
          + "Project"     = "Dotz Challenge"
          + "Team"        = "dotz"
        }
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      + versioning {
          + enabled    = (known after apply)
          + mfa_delete = (known after apply)
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

aws_s3_bucket.dotz_input: Creating...
aws_s3_bucket.dotz_input: Creation complete after 2s [id=dotz-input]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Após aplicar o `terraform` o bucket deverá ser provisionado na `AWS`

![terraform-apply-bucket](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/terraform-apply-bucket.png)
