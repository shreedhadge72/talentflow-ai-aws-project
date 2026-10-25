# Planned architecture

Local prototype: Browser → Flask → SQLite; optional resume files stored locally.

Planned AWS version: Internet → public Application Load Balancer → application compute in private subnets → private RDS. Resumes use a private S3 bucket. SQS/Lambda can process events; SNS can notify; CloudWatch collects logs, metrics and alarms. IAM roles grant least-privilege access.

This is a design plan, not evidence of deployment. Update status only after each resource is deployed and tested. CloudFormation will be used; Terraform is intentionally excluded.
