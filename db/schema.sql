-- Demonstration schema; Flask creates the local SQLite table automatically.
CREATE TABLE applications (
  id INTEGER PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(200) NOT NULL,
  job_title VARCHAR(200) NOT NULL,
  resume_filename VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
