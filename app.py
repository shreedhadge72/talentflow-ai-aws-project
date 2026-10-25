from pathlib import Path
import os
import sqlite3
from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "instance"
UPLOAD_DIR = ROOT / "uploads"
DB_PATH = DATA_DIR / "talentflow.sqlite3"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "local-demo-only-change-me")
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

JOBS = [
    {"title": "Junior Cloud Engineer", "team": "Cloud Platform", "location": "Remote / India", "kind": "Full-time"},
    {"title": "Python Developer Intern", "team": "Engineering", "location": "Hybrid", "kind": "Internship"},
    {"title": "DevOps Trainee", "team": "Platform Engineering", "location": "Pune, India", "kind": "Full-time"},
]

def db():
    DATA_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with db() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            job_title TEXT NOT NULL,
            resume_filename TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

@app.route("/")
def index():
    return render_template("index.html", jobs=JOBS)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/apply", methods=["POST"])
def apply():
    name = request.form.get("full_name", "").strip()
    email = request.form.get("email", "").strip()
    job = request.form.get("job_title", "").strip()
    resume = request.files.get("resume")
    if not name or not email or job not in {j["title"] for j in JOBS}:
        flash("Complete all required fields and choose a listed job.", "error")
        return redirect(url_for("index"))
    saved = None
    if resume and resume.filename:
        filename = secure_filename(resume.filename)
        if "." not in filename or filename.rsplit(".", 1)[1].lower() not in ALLOWED_EXTENSIONS:
            flash("Resume must be PDF, DOC, or DOCX.", "error")
            return redirect(url_for("index"))
        UPLOAD_DIR.mkdir(exist_ok=True)
        destination = UPLOAD_DIR / (os.urandom(4).hex() + "_" + filename)
        resume.save(destination)
        saved = destination.name
    with db() as conn:
        conn.execute(
            "INSERT INTO applications (full_name, email, job_title, resume_filename) VALUES (?, ?, ?, ?)",
            (name, email, job, saved),
        )
    flash("Sample application saved locally. Do not submit real personal data.", "success")
    return redirect(url_for("index"))

@app.errorhandler(413)
def too_large(_error):
    flash("File too large. Maximum size is 5 MB.", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=False)
