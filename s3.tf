# Componentes
# - s3_bucket
# - vpc_endpoint
# - vpc_endpoint_route_table_association
# - s3_bucket_object

resource "aws_s3_bucket" "dotz_input" {
  bucket = "dotz-input"
  acl    = "private"
  tags   = var.tags
}

resource "aws_vpc_endpoint" "s3" {
  vpc_id       = var.vpc
  service_name = "com.amazonaws.us-east-1.s3"
  tags         = var.tags
}

resource "aws_vpc_endpoint_route_table_association" "private_s3" {
  vpc_endpoint_id = aws_vpc_endpoint.s3.id
  route_table_id  = var.route_table
}

resource "aws_s3_bucket_object" "raw" {
  bucket = aws_s3_bucket.dotz_input.id
  key    = "raw/"
}

resource "aws_s3_bucket_object" "job_price_quote" {
  bucket = var.glue-scripts
  source = "./jobs/job_price_quote.py"
  key    = "root/job_price_quote.py"
  etag   = filemd5("./jobs/job_price_quote.py")
}

resource "aws_s3_bucket_object" "job_bill_of_materials" {
  bucket = var.glue-scripts
  source = "./jobs/job_bill_of_materials.py"
  key    = "root/job_bill_of_materials.py"
  etag   = filemd5("./jobs/job_bill_of_materials.py")
}

resource "aws_s3_bucket_object" "job_comp_boss" {
  bucket = var.glue-scripts
  source = "./jobs/job_comp_boss.py"
  key    = "root/job_comp_boss.py"
  etag   = filemd5("./jobs/job_comp_boss.py")
}
