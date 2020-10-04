resource "aws_glue_catalog_database" "dotz_catalog_database" {
  name        = "${var.database_name}_raw"
  description = "Database Raw - files CSV"
}

resource "aws_glue_crawler" "dotz_raw" {
  name          = "${var.database_name}_raw"
  database_name = aws_glue_catalog_database.dotz_catalog_database.name
  role          = aws_iam_role.dotz.arn
  tags          = var.tags
  s3_target {
    path = "s3://${aws_s3_bucket.dotz_input.id}/raw"
  }
  schema_change_policy {
    delete_behavior = "DEPRECATE_IN_DATABASE"
    update_behavior = "UPDATE_IN_DATABASE"
  }
}

resource "aws_glue_connection" "dotz_connection" {
  connection_properties = {
    JDBC_CONNECTION_URL = "jdbc:postgresql://${aws_db_instance.this.endpoint}/${var.database_name}"
    PASSWORD            = trimspace(file("${path.module}/.secrets.txt"))
    USERNAME            = var.username
  }
  name            = "dotz_connection"
  connection_type = "JDBC"
  physical_connection_requirements {
    availability_zone      = var.availability_zone
    security_group_id_list = [aws_security_group.this.id]
    subnet_id              = var.subnet
  }
}

resource "aws_glue_job" "job_comp_boss" {
  name              = "job_comp_boss"
  role_arn          = aws_iam_role.dotz.arn
  glue_version      = "2.0"
  number_of_workers = 10
  worker_type       = "G.1X"
  connections       = [aws_glue_connection.dotz_connection.name]
  command {
    script_location = "s3://${var.glue-scripts}/root/job_comp_boss.py"
  }
  default_arguments = {
    "--job-language" = "python"
    "--TempDir"      = "s3://${var.glue-temporary}/root"
  }
}

resource "aws_glue_job" "job_price_quote" {
  name              = "job_price_quote"
  role_arn          = aws_iam_role.dotz.arn
  glue_version      = "2.0"
  number_of_workers = 10
  worker_type       = "G.1X"
  connections       = [aws_glue_connection.dotz_connection.name]
  command {
    script_location = "s3://${var.glue-scripts}/root/job_price_quote.py"
  }
  default_arguments = {
    "--job-language" = "python"
    "--TempDir"      = "s3://${var.glue-temporary}/root"
  }
}

resource "aws_glue_job" "job_bill_of_materials" {
  name              = "job_bill_of_materials"
  role_arn          = aws_iam_role.dotz.arn
  glue_version      = "2.0"
  number_of_workers = 10
  worker_type       = "G.1X"
  connections       = [aws_glue_connection.dotz_connection.name]
  command {
    script_location = "s3://${var.glue-scripts}/root/job_bill_of_materials.py"
  }
  default_arguments = {
    "--job-language" = "python"
    "--TempDir"      = "s3://${var.glue-temporary}/root"
  }
}
