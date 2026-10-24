
# TalentFlow AI — AWS Cloud Platform

**Project by:** Shree Dhadge

## Overview

TalentFlow AI is an AI-powered recruitment platform project
focused on building secure, scalable and highly available
cloud infrastructure on Amazon Web Services (AWS).

The platform is designed to support candidate applications,
resume storage, background processing, recruiter notifications
and application monitoring.

## Architecture

![TalentFlow AI AWS Architecture](docs/diagrams/architecture.png)

## AWS Services

- Amazon VPC
- Amazon EC2
- Elastic Load Balancing (ALB)
- EC2 Auto Scaling
- Amazon S3
- Amazon RDS
- AWS Lambda
- Amazon SQS
- Amazon SNS
- Amazon EventBridge
- Amazon CloudWatch
- AWS IAM
- AWS CloudFormation
- Amazon ECR and Docker

Additional services such as CloudFront, Route 53, CloudTrail
and AWS Config will be included where implemented.

## Main Features

- Secure AWS network architecture
- Load balancing and automatic scaling
- Private database connectivity
- Secure resume storage
- Event-driven background processing
- Monitoring, logs and alarms
- Infrastructure as Code using CloudFormation

## Repository Structure

- `app/` — Application source code
- `cloudformation/` — AWS infrastructure templates
- `lambda/` — Background processing functions
- `iam/` — IAM policy definitions
- `db/` — Database schema
- `scripts/` — Deployment and testing scripts
- `docs/` — Architecture and project documentation

## Project Status

Implementation in progress.

Only verified and deployed features will be marked as completed.

## Security

Never commit AWS credentials, private keys, database passwords,
environment files or personal candidate data.

## Author

Shree Dhadge
