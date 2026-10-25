# Troubleshooting

- Copy the complete error and the command that produced it.
- Run `Get-Location` and `Get-ChildItem` to confirm the current folder.
- Check `py --version`, `python --version`, and `python -m pip --version`.
- Confirm `(.venv)` appears in the PowerShell prompt.
- For app errors, check the PowerShell window running `python app.py`.
- For Docker errors, confirm Docker Desktop is running.
- For AWS errors, check the region, IAM permissions, and CloudFormation stack Events.
- Never share access keys, passwords, tokens, or private keys.
