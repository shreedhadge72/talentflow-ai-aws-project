# TalentFlow AI — AWS Cloud Platform

**Author:** Shree Dhadge  
**Status:** Sample app starter. AWS deployment is not yet verified.

This is a student-built sample recruitment website inspired by the supplied project guide. It is not the original TalentFlow application and does not use a real AI model yet.

## Local run (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`. Health check: `http://127.0.0.1:5000/health`.

If activation is blocked:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Features
- Sample job listings
- Candidate application form
- Optional local resume upload (PDF, DOC, DOCX; max 5 MB)
- SQLite local demo database
- `/health` endpoint
- Docker starter

## Planned AWS design
Internet → public Application Load Balancer → application compute in private subnets → private RDS. Resumes use a private S3 bucket. SQS/Lambda can process events and SNS can notify. CloudWatch provides logs and alarms.

## Safety and honesty
Use fictional test data only. Never commit credentials, `.env`, private keys, or real resumes. This starter is not production-ready. Only mark AWS services as deployed after you actually deploy and verify them. Terraform is intentionally not used; infrastructure will be written in CloudFormation.

## Structure
```text
app.py
requirements.txt
Dockerfile
.dockerignore
.gitignore
app/templates/index.html
app/static/style.css
db/schema.sql
cloudformation/README.md
lambda/README.md
iam/README.md
scripts/cleanup-checklist.md
docs/setup-windows.md
docs/architecture.md
docs/troubleshooting.md
docs/diagrams/README.md
docs/evidence/README.md
```
