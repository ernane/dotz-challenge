# Terraform

## Demonstração de como subir a infraestrutura necessária para esse desafio

[![asciicast](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/terraform.gif)](https://asciinema.org/a/363467)

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
https://app.terraform.io/app/dotz-challenge/dotz/runs/run-UaHrsna9EK1CfDxw

Waiting for the plan to start...

Terraform v0.12.29
Configuring remote state backend...
Initializing Terraform configuration...
2020/10/04 16:33:22 [DEBUG] Using modified User-Agent: Terraform/0.12.29 TFC/1041834820
Refreshing Terraform state in-memory prior to plan...
The refreshed state will be used to calculate this plan, but will not be
persisted to local or remote state storage.


------------------------------------------------------------------------

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_db_instance.this will be created
  + resource "aws_db_instance" "this" {
      + address                               = (known after apply)
      + allocated_storage                     = 10
      + apply_immediately                     = (known after apply)
      + arn                                   = (known after apply)
      + auto_minor_version_upgrade            = true
      + availability_zone                     = (known after apply)
      + backup_retention_period               = (known after apply)
      + backup_window                         = (known after apply)
      + ca_cert_identifier                    = (known after apply)
      + character_set_name                    = (known after apply)
      + copy_tags_to_snapshot                 = false
      + db_subnet_group_name                  = "rds-public-subnet-group"
      + delete_automated_backups              = true
      + endpoint                              = (known after apply)
      + engine                                = "postgres"
      + engine_version                        = "12.4"
      + final_snapshot_identifier             = "dotz-challenge-db-backup"
      + hosted_zone_id                        = (known after apply)
      + id                                    = (known after apply)
      + identifier                            = "dotz-challenge-db"
      + identifier_prefix                     = (known after apply)
      + instance_class                        = "db.t2.micro"
      + kms_key_id                            = (known after apply)
      + license_model                         = (known after apply)
      + maintenance_window                    = (known after apply)
      + monitoring_interval                   = 0
      + monitoring_role_arn                   = (known after apply)
      + multi_az                              = false
      + name                                  = "dotz_challenge"
      + option_group_name                     = (known after apply)
      + parameter_group_name                  = (known after apply)
      + password                              = (sensitive value)
      + performance_insights_enabled          = false
      + performance_insights_kms_key_id       = (known after apply)
      + performance_insights_retention_period = (known after apply)
      + port                                  = 5432
      + publicly_accessible                   = true
      + replicas                              = (known after apply)
      + resource_id                           = (known after apply)
      + skip_final_snapshot                   = true
      + status                                = (known after apply)
      + storage_type                          = "gp2"
      + timezone                              = (known after apply)
      + username                              = "dotz"
      + vpc_security_group_ids                = (known after apply)
    }

  # aws_db_subnet_group.rds-public-subnet will be created
  + resource "aws_db_subnet_group" "rds-public-subnet" {
      + arn         = (known after apply)
      + description = "Managed by Terraform"
      + id          = (known after apply)
      + name        = "rds-public-subnet-group"
      + name_prefix = (known after apply)
      + subnet_ids  = [
          + "subnet-0c1ff953",
          + "subnet-0d83aa33",
          + "subnet-4fec0929",
          + "subnet-533d881e",
          + "subnet-7c12cd72",
          + "subnet-8641a1a7",
        ]
    }

  # aws_glue_catalog_database.dotz_catalog_database will be created
  + resource "aws_glue_catalog_database" "dotz_catalog_database" {
      + arn         = (known after apply)
      + catalog_id  = (known after apply)
      + description = "Database Raw - files CSV"
      + id          = (known after apply)
      + name        = "dotz_challenge_raw"
    }

  # aws_glue_connection.dotz_connection will be created
  + resource "aws_glue_connection" "dotz_connection" {
      + arn                   = (known after apply)
      + catalog_id            = (known after apply)
      + connection_properties = (sensitive value)
      + connection_type       = "JDBC"
      + id                    = (known after apply)
      + name                  = "dotz_connection"

      + physical_connection_requirements {
          + availability_zone      = "us-east-1c"
          + security_group_id_list = (known after apply)
          + subnet_id              = "subnet-0c1ff953"
        }
    }

  # aws_glue_crawler.dotz_raw will be created
  + resource "aws_glue_crawler" "dotz_raw" {
      + arn           = (known after apply)
      + database_name = "dotz_challenge_raw"
      + id            = (known after apply)
      + name          = "dotz_challenge_raw"
      + role          = (known after apply)
      + tags          = {
          + "Author"      = "ernane.sena@gmail.com"
          + "Environment" = "development"
          + "Project"     = "Dotz Challenge"
          + "Team"        = "dotz"
        }

      + s3_target {
          + path = (known after apply)
        }

      + schema_change_policy {
          + delete_behavior = "DEPRECATE_IN_DATABASE"
          + update_behavior = "UPDATE_IN_DATABASE"
        }
    }

  # aws_glue_job.job_bill_of_materials will be created
  + resource "aws_glue_job" "job_bill_of_materials" {
      + arn               = (known after apply)
      + connections       = [
          + "dotz_connection",
        ]
      + default_arguments = {
          + "--TempDir"      = "s3://aws-glue-temporary-020095487191-us-east-1/root"
          + "--job-language" = "python"
        }
      + glue_version      = "2.0"
      + id                = (known after apply)
      + max_capacity      = (known after apply)
      + name              = "job_bill_of_materials"
      + number_of_workers = 10
      + role_arn          = (known after apply)
      + timeout           = 2880
      + worker_type       = "G.1X"

      + command {
          + name            = "glueetl"
          + python_version  = (known after apply)
          + script_location = "s3://aws-glue-scripts-020095487191-us-east-1/root/job_bill_of_materials.py"
        }

      + execution_property {
          + max_concurrent_runs = (known after apply)
        }

      + notification_property {
          + notify_delay_after = (known after apply)
        }
    }

  # aws_glue_job.job_comp_boss will be created
  + resource "aws_glue_job" "job_comp_boss" {
      + arn               = (known after apply)
      + connections       = [
          + "dotz_connection",
        ]
      + default_arguments = {
          + "--TempDir"      = "s3://aws-glue-temporary-020095487191-us-east-1/root"
          + "--job-language" = "python"
        }
      + glue_version      = "2.0"
      + id                = (known after apply)
      + max_capacity      = (known after apply)
      + name              = "job_comp_boss"
      + number_of_workers = 10
      + role_arn          = (known after apply)
      + timeout           = 2880
      + worker_type       = "G.1X"

      + command {
          + name            = "glueetl"
          + python_version  = (known after apply)
          + script_location = "s3://aws-glue-scripts-020095487191-us-east-1/root/job_comp_boss.py"
        }

      + execution_property {
          + max_concurrent_runs = (known after apply)
        }

      + notification_property {
          + notify_delay_after = (known after apply)
        }
    }

  # aws_glue_job.job_price_quote will be created
  + resource "aws_glue_job" "job_price_quote" {
      + arn               = (known after apply)
      + connections       = [
          + "dotz_connection",
        ]
      + default_arguments = {
          + "--TempDir"      = "s3://aws-glue-temporary-020095487191-us-east-1/root"
          + "--job-language" = "python"
        }
      + glue_version      = "2.0"
      + id                = (known after apply)
      + max_capacity      = (known after apply)
      + name              = "job_price_quote"
      + number_of_workers = 10
      + role_arn          = (known after apply)
      + timeout           = 2880
      + worker_type       = "G.1X"

      + command {
          + name            = "glueetl"
          + python_version  = (known after apply)
          + script_location = "s3://aws-glue-scripts-020095487191-us-east-1/root/job_price_quote.py"
        }

      + execution_property {
          + max_concurrent_runs = (known after apply)
        }

      + notification_property {
          + notify_delay_after = (known after apply)
        }
    }

  # aws_iam_policy.policy will be created
  + resource "aws_iam_policy" "policy" {
      + arn         = (known after apply)
      + description = "This policy will be used for Glue Crawler and Job execution. Please do NOT delete!"
      + id          = (known after apply)
      + name        = "AWSGlueServicePolicy-PutAccess"
      + path        = "/"
      + policy      = jsonencode(
            {
              + Statement = [
                  + {
                      + Action   = [
                          + "s3:GetObject",
                          + "s3:PutObject",
                        ]
                      + Effect   = "Allow"
                      + Resource = [
                          + "arn:aws:s3:::dotz-input*",
                        ]
                    },
                ]
              + Version   = "2012-10-17"
            }
        )
    }

  # aws_iam_role.dotz will be created
  + resource "aws_iam_role" "dotz" {
      + arn                   = (known after apply)
      + assume_role_policy    = jsonencode(
            {
              + Statement = [
                  + {
                      + Action    = "sts:AssumeRole"
                      + Effect    = "Allow"
                      + Principal = {
                          + Service = "glue.amazonaws.com"
                        }
                      + Sid       = ""
                    },
                ]
              + Version   = "2012-10-17"
            }
        )
      + create_date           = (known after apply)
      + force_detach_policies = false
      + id                    = (known after apply)
      + max_session_duration  = 3600
      + name                  = "AWSGlueServiceRole-Dotz"
      + path                  = "/service-role/"
      + tags                  = {
          + "Author"      = "ernane.sena@gmail.com"
          + "Environment" = "development"
          + "Project"     = "Dotz Challenge"
          + "Team"        = "dotz"
        }
      + unique_id             = (known after apply)
    }

  # aws_iam_role_policy_attachment.glue_service_attach will be created
  + resource "aws_iam_role_policy_attachment" "glue_service_attach" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
      + role       = "AWSGlueServiceRole-Dotz"
    }

  # aws_iam_role_policy_attachment.s3_put_access_attach will be created
  + resource "aws_iam_role_policy_attachment" "s3_put_access_attach" {
      + id         = (known after apply)
      + policy_arn = (known after apply)
      + role       = "AWSGlueServiceRole-Dotz"
    }

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

  # aws_s3_bucket_object.job_bill_of_materials will be created
  + resource "aws_s3_bucket_object" "job_bill_of_materials" {
      + acl                    = "private"
      + bucket                 = "aws-glue-scripts-020095487191-us-east-1"
      + content_type           = (known after apply)
      + etag                   = "78c703838ce471dcc0ab56a1e3cf108e"
      + force_destroy          = false
      + id                     = (known after apply)
      + key                    = "root/job_bill_of_materials.py"
      + server_side_encryption = (known after apply)
      + source                 = "./jobs/job_bill_of_materials.py"
      + storage_class          = (known after apply)
      + version_id             = (known after apply)
    }

  # aws_s3_bucket_object.job_comp_boss will be created
  + resource "aws_s3_bucket_object" "job_comp_boss" {
      + acl                    = "private"
      + bucket                 = "aws-glue-scripts-020095487191-us-east-1"
      + content_type           = (known after apply)
      + etag                   = "dc4dca470919dfbb964048ba10b2718d"
      + force_destroy          = false
      + id                     = (known after apply)
      + key                    = "root/job_comp_boss.py"
      + server_side_encryption = (known after apply)
      + source                 = "./jobs/job_comp_boss.py"
      + storage_class          = (known after apply)
      + version_id             = (known after apply)
    }

  # aws_s3_bucket_object.job_price_quote will be created
  + resource "aws_s3_bucket_object" "job_price_quote" {
      + acl                    = "private"
      + bucket                 = "aws-glue-scripts-020095487191-us-east-1"
      + content_type           = (known after apply)
      + etag                   = "be683f645d81d6c02532954740079360"
      + force_destroy          = false
      + id                     = (known after apply)
      + key                    = "root/job_price_quote.py"
      + server_side_encryption = (known after apply)
      + source                 = "./jobs/job_price_quote.py"
      + storage_class          = (known after apply)
      + version_id             = (known after apply)
    }

  # aws_s3_bucket_object.raw will be created
  + resource "aws_s3_bucket_object" "raw" {
      + acl                    = "private"
      + bucket                 = (known after apply)
      + content_type           = (known after apply)
      + etag                   = (known after apply)
      + force_destroy          = false
      + id                     = (known after apply)
      + key                    = "raw/"
      + server_side_encryption = (known after apply)
      + storage_class          = (known after apply)
      + version_id             = (known after apply)
    }

  # aws_security_group.this will be created
  + resource "aws_security_group" "this" {
      + arn                    = (known after apply)
      + description            = "RDS postgres servers (terraform-managed)"
      + egress                 = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 0
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "-1"
              + security_groups  = []
              + self             = false
              + to_port          = 0
            },
        ]
      + id                     = (known after apply)
      + ingress                = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 0
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "-1"
              + security_groups  = []
              + self             = false
              + to_port          = 0
            },
        ]
      + name                   = "dotz"
      + owner_id               = (known after apply)
      + revoke_rules_on_delete = false
      + vpc_id                 = "vpc-af4c7dd5"
    }

  # aws_vpc_endpoint.s3 will be created
  + resource "aws_vpc_endpoint" "s3" {
      + arn                   = (known after apply)
      + cidr_blocks           = (known after apply)
      + dns_entry             = (known after apply)
      + id                    = (known after apply)
      + network_interface_ids = (known after apply)
      + owner_id              = (known after apply)
      + policy                = (known after apply)
      + prefix_list_id        = (known after apply)
      + private_dns_enabled   = false
      + requester_managed     = (known after apply)
      + route_table_ids       = (known after apply)
      + security_group_ids    = (known after apply)
      + service_name          = "com.amazonaws.us-east-1.s3"
      + state                 = (known after apply)
      + subnet_ids            = (known after apply)
      + tags                  = {
          + "Author"      = "ernane.sena@gmail.com"
          + "Environment" = "development"
          + "Project"     = "Dotz Challenge"
          + "Team"        = "dotz"
        }
      + vpc_endpoint_type     = "Gateway"
      + vpc_id                = "vpc-af4c7dd5"
    }

  # aws_vpc_endpoint_route_table_association.private_s3 will be created
  + resource "aws_vpc_endpoint_route_table_association" "private_s3" {
      + id              = (known after apply)
      + route_table_id  = "rtb-04ca767a"
      + vpc_endpoint_id = (known after apply)
    }

Plan: 20 to add, 0 to change, 0 to destroy.
```

## Aplicando as modificações com o `terraform`

```bash
terraform apply -auto-approve
```

A saída desse comando, deverá produzir uma saída parecida como essa:

```bash
Plan: 20 to add, 0 to change, 0 to destroy.

aws_security_group.this: Creating...
aws_glue_catalog_database.dotz_catalog_database: Creating...
aws_iam_role.dotz: Creating...
aws_vpc_endpoint.s3: Creating...
aws_s3_bucket_object.job_comp_boss: Creating...
aws_s3_bucket_object.job_price_quote: Creating...
aws_s3_bucket_object.job_bill_of_materials: Creating...
aws_db_subnet_group.rds-public-subnet: Creating...
aws_iam_policy.policy: Creating...
aws_s3_bucket.dotz_input: Creating...
aws_s3_bucket_object.job_comp_boss: Creation complete after 0s [id=root/job_comp_boss.py]
aws_s3_bucket_object.job_price_quote: Creation complete after 0s [id=root/job_price_quote.py]
aws_s3_bucket_object.job_bill_of_materials: Creation complete after 0s [id=root/job_bill_of_materials.py]
aws_glue_catalog_database.dotz_catalog_database: Creation complete after 0s [id=020095487191:dotz_challenge_raw]
aws_db_subnet_group.rds-public-subnet: Creation complete after 1s [id=rds-public-subnet-group]
aws_iam_role.dotz: Creation complete after 1s [id=AWSGlueServiceRole-Dotz]
aws_iam_role_policy_attachment.glue_service_attach: Creating...
aws_s3_bucket.dotz_input: Creation complete after 1s [id=dotz-input]
aws_glue_crawler.dotz_raw: Creating...
aws_s3_bucket_object.raw: Creating...
aws_security_group.this: Creation complete after 2s [id=sg-0f29f7f987bc4e49b]
aws_db_instance.this: Creating...
aws_s3_bucket_object.raw: Creation complete after 0s [id=raw/]
aws_iam_policy.policy: Creation complete after 2s [id=arn:aws:iam::020095487191:policy/AWSGlueServicePolicy-PutAccess]
aws_iam_role_policy_attachment.s3_put_access_attach: Creating...
aws_iam_role_policy_attachment.glue_service_attach: Creation complete after 2s [id=AWSGlueServiceRole-Dotz-20201004163408204000000001]
aws_iam_role_policy_attachment.s3_put_access_attach: Creation complete after 2s [id=AWSGlueServiceRole-Dotz-20201004163409011900000002]
aws_vpc_endpoint.s3: Creation complete after 6s [id=vpce-0b8ec4a9031fd52fa]
aws_vpc_endpoint_route_table_association.private_s3: Creating...
aws_vpc_endpoint_route_table_association.private_s3: Creation complete after 0s [id=a-vpce-0b8ec4a9031fd52fa1334317113]
aws_glue_crawler.dotz_raw: Creation complete after 9s [id=dotz_challenge_raw]
aws_db_instance.this: Still creating... [10s elapsed]
aws_db_instance.this: Still creating... [20s elapsed]
aws_db_instance.this: Still creating... [30s elapsed]
aws_db_instance.this: Still creating... [40s elapsed]
aws_db_instance.this: Still creating... [50s elapsed]
aws_db_instance.this: Still creating... [1m0s elapsed]
aws_db_instance.this: Still creating... [1m10s elapsed]
aws_db_instance.this: Still creating... [1m20s elapsed]
aws_db_instance.this: Still creating... [1m30s elapsed]
aws_db_instance.this: Still creating... [1m40s elapsed]
aws_db_instance.this: Still creating... [1m50s elapsed]
aws_db_instance.this: Still creating... [2m0s elapsed]
aws_db_instance.this: Still creating... [2m10s elapsed]
aws_db_instance.this: Still creating... [2m20s elapsed]
aws_db_instance.this: Still creating... [2m30s elapsed]
aws_db_instance.this: Still creating... [2m40s elapsed]
aws_db_instance.this: Still creating... [2m50s elapsed]
aws_db_instance.this: Still creating... [3m0s elapsed]
aws_db_instance.this: Still creating... [3m10s elapsed]
aws_db_instance.this: Still creating... [3m20s elapsed]
aws_db_instance.this: Still creating... [3m30s elapsed]
aws_db_instance.this: Still creating... [3m40s elapsed]
aws_db_instance.this: Creation complete after 3m45s [id=dotz-challenge-db]
aws_glue_connection.dotz_connection: Creating...
aws_glue_connection.dotz_connection: Creation complete after 0s [id=020095487191:dotz_connection]
aws_glue_job.job_bill_of_materials: Creating...
aws_glue_job.job_comp_boss: Creating...
aws_glue_job.job_price_quote: Creating...
aws_glue_job.job_price_quote: Creation complete after 0s [id=job_price_quote]
aws_glue_job.job_comp_boss: Creation complete after 0s [id=job_comp_boss]
aws_glue_job.job_bill_of_materials: Creation complete after 0s [id=job_bill_of_materials]

Apply complete! Resources: 20 added, 0 changed, 0 destroyed.
```

Após aplicar o `terraform` o bucket deverá ser provisionado na `AWS`

![terraform-apply-bucket](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/terraform-apply-bucket.png)
