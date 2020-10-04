# Componentes
# - iam_policy
# - iam_role
# - iam_role_policy_attachment

resource "aws_iam_policy" "policy" {
  name        = "AWSGlueServicePolicy-PutAccess"
  path        = "/"
  description = "This policy will be used for Glue Crawler and Job execution. Please do NOT delete!"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::dotz-input*"
      ]
    }
  ]
}
EOF
}

resource "aws_iam_role" "dotz" {
  name = "AWSGlueServiceRole-Dotz"
  tags = var.tags
  path = "/service-role/"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "glue_service_attach" {
  role       = aws_iam_role.dotz.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}

resource "aws_iam_role_policy_attachment" "s3_put_access_attach" {
  role       = aws_iam_role.dotz.name
  policy_arn = aws_iam_policy.policy.arn
}
