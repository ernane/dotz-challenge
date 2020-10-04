variable "region" {
  default     = "us-east-1"
  type        = string
  description = "Default region AWS"
}

variable "tags" {
  default = {
    Environment = "development"
    Project     = "Dotz Challenge"
    Team        = "dotz"
    Author      = "ernane.sena@gmail.com"
  }
  type        = map(string)
  description = "Extra tags to attach to AWS resources"
}

variable "glue-scripts" {
  default     = "aws-glue-scripts-020095487191-us-east-1"
  type        = string
  description = "Bucket for scripts Glue"
}

variable "glue-temporary" {
  default     = "aws-glue-temporary-020095487191-us-east-1"
  type        = string
  description = "Bucket temporary Glue"
}

variable "vpc" {
  default     = "vpc-af4c7dd5"
  type        = string
  description = "default RDS virtual private cloud"
}

variable "route_table" {
  default     = "rtb-04ca767a"
  type        = string
  description = "Route Table ID"
}

variable "database_name" {
  default     = "dotz_challenge"
  type        = string
  description = "Database and Crawler name"
}

variable "instance_class" {
  default     = "db.t2.micro"
  description = "The instance type of the RDS instance"
  type        = string
}

variable "username" {
  description = "Username for the master DB user"
  type        = string
  default     = "dotz"
}

variable "availability_zone" {
  description = "Availability Zone"
  type        = string
  default     = "us-east-1c"
}

# variable "security_groups" {
#   description = "A list of VPC security groups IDs"
#   type        = list(string)
#   default     = ["sg-0c205c7ea39e6bc01"]
# }

variable "subnet" {
  description = "Subnet ID"
  type        = string
  default     = "subnet-0c1ff953"
}

variable "subnet_ids" {
  description = "A list of VPC subnet IDs"
  type        = list(string)
  default = [
    "subnet-0c1ff953",
    "subnet-0d83aa33",
    "subnet-4fec0929",
    "subnet-533d881e",
    "subnet-7c12cd72",
    "subnet-8641a1a7"
  ]
}

variable "identifier" {
  description = "The name of the RDS instance, if omitted, Terraform will assign a random, unique identifier"
  type        = string
  default     = "dotz-challenge-db"
}

variable "allocated_storage" {
  description = "The allocated storage in gigabytes"
  type        = number
  default     = 10
}

variable "engine" {
  description = "The database engine to use"
  type        = string
  default     = "postgres"
}

variable "engine_version" {
  description = "The engine version to use"
  type        = string
  default     = "12.4"
}

variable "multi_az" {
  description = "Specifies if the RDS instance is multi-AZ"
  type        = bool
  default     = false
}

variable "port" {
  description = "The port on which the DB accepts connections"
  type        = number
  default     = 5432
}

variable "publicly_accessible" {
  description = "Bool to control if instance is publicly accessible"
  type        = bool
  default     = true
}

variable "skip_final_snapshot" {
  description = "skip_final_snapshot"
  type        = bool
  default     = true
}

variable "storage_type" {
  description = "One of 'standard' (magnetic), 'gp2' (general purpose SSD), or 'io1' (provisioned IOPS SSD). The default is 'io1' if iops is specified, 'standard' if not. Note that this behaviour is different from the AWS web console, where the default is 'gp2'."
  type        = string
  default     = "gp2"
}
