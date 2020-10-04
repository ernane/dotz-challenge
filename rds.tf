resource "aws_db_subnet_group" "rds-public-subnet" {
  name       = "rds-public-subnet-group"
  subnet_ids = var.subnet_ids
}

resource "aws_security_group" "this" {
  name        = "dotz"
  description = "RDS postgres servers (terraform-managed)"
  vpc_id      = var.vpc

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "this" {
  allocated_storage         = var.allocated_storage
  db_subnet_group_name      = aws_db_subnet_group.rds-public-subnet.name
  engine                    = var.engine
  engine_version            = var.engine_version
  identifier                = var.identifier
  instance_class            = var.instance_class
  multi_az                  = var.multi_az
  name                      = var.database_name
  password                  = trimspace(file("${path.module}/.secrets.txt"))
  port                      = var.port
  publicly_accessible       = var.publicly_accessible
  storage_type              = var.storage_type
  username                  = var.username
  vpc_security_group_ids    = [aws_security_group.this.id]
  final_snapshot_identifier = "${var.identifier}-backup"
  skip_final_snapshot       = var.skip_final_snapshot
}
