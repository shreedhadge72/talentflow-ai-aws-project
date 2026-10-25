# Windows setup

1. Install Python from python.org; enable **Add Python to PATH**.
2. Install Git for Windows.
3. Install Docker Desktop if you plan to test containers; start it before using Docker.
4. Install AWS CLI v2 for later AWS steps.
5. Open a new PowerShell window and verify:
   `py --version`, `python --version`, `git --version`, `docker --version`, `aws --version`.
6. In the repository root run:
   `py -m venv .venv`
   ` .\.venv\Scripts\Activate.ps1`
   `python -m pip install --upgrade pip`
   `pip install -r requirements.txt`
   `python app.py`
7. Open `http://127.0.0.1:5000`; health check `http://127.0.0.1:5000/health`.
8. Stop the server with Ctrl+C in PowerShell.

If activation is blocked:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
then activate again.

Common errors:
- `py` not recognized: reinstall Python with PATH enabled, then reopen PowerShell.
- `No module named flask`: activate `.venv`, then run `pip install -r requirements.txt`.
- `requirements.txt` missing: `Get-Location` and `Get-ChildItem`; move to the repository root.
- Port busy: stop another server with Ctrl+C or run `$env:PORT="5001"; python app.py`.
- Docker daemon error: start Docker Desktop and wait until it is running.
- Never paste AWS credentials, passwords, session tokens, or private keys into chat.
