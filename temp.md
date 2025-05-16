# 🛠 Python Project Structure: Common Utils + Business Scheduler

## ✅ Project Overview

This structure separates:

1. **`common-utils`** — a reusable Python package with FTP, logging, file handling, and secret management utilities.
2. **`ftp-scheduler`** — a business logic project using `common-utils` and implementing a scheduler to download files from an FTP server.

---

## 1️⃣ `common-utils` Package

### Purpose

Reusable utility functions that can be uploaded to Artifactory or PyPI and reused across projects.

### Features

* FTP utilities (`ftp_utils`)
* File utilities (`file_utils`)
* Logger setup (`logger_utils`)
* Secrets handling utilities (`secret_utils`)

### Project Structure

```
common-utils/
├── pyproject.toml
├── README.md
├── src/
│   └── common_utils/
│       ├── __init__.py
│       ├── ftp_utils.py
│       ├── logger_utils.py
│       ├── file_utils.py
│       └── secret_utils.py
└── tests/
    └── test_secret_utils.py
```

### Example Files

#### `secret_utils.py`

```python
import os
from cryptography.fernet import Fernet

def load_secret_key_from_file(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

def decrypt_value(encrypted_value, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_value.encode()).decode()

def decrypt_value_from_env(encrypted_value):
    key_path = os.getenv('SECRET_KEY_PATH')
    if not key_path:
        raise ValueError("SECRET_KEY_PATH not set in environment variables.")
    key = load_secret_key_from_file(key_path)
    return decrypt_value(encrypted_value, key)
```

### How to Build & Install

1. Build the wheel package:

   ```bash
   python -m build
   ```
2. Upload the wheel to Artifactory or PyPI.
3. Install it in other projects:

   ```bash
   pip install common-utils
   ```

### Usage Example

```python
from common_utils import download_file, decrypt_value_from_env

download_file("ftp.example.com", "user", "pass", "/remote/file.txt", "./file.txt")
secret = decrypt_value_from_env("gAAAAABj...")
print(secret)
```

---

## 2️⃣ `ftp-scheduler` Project

### Purpose

Schedules file downloads from FTP using the utilities from `common-utils`.

### Project Structure

```
ftp-scheduler/
├── pyproject.toml
├── requirements.txt
├── src/
│   └── ftp_scheduler/
│       ├── __init__.py
│       ├── main_scheduler.py
│       └── config.py
└── tests/
    └── test_scheduler.py
```

### Example Files

#### `main_scheduler.py`

```python
import schedule
import time
from common_utils.ftp_utils import download_file

def job():
    print("Running FTP download job...")
    download_file("ftp.example.com", "user", "pass", "/remote/path/file.txt", "./file.txt")

if __name__ == "__main__":
    schedule.every(10).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
```

### Running the Project

```bash
python src/ftp_scheduler/main_scheduler.py
```

---

## 📦 Best Practices Summary

| Task                       | Recommendation                              |
| -------------------------- | ------------------------------------------- |
| Reusable utilities         | Isolated in `common-utils` package          |
| Project-specific logic     | In `ftp-scheduler` project only             |
| Secrets handling           | Via `secret_utils` in `common-utils`        |
| Dependency management      | Use `pyproject.toml` and `requirements.txt` |
| Build & release automation | Use Jenkins pipeline to build & deploy      |

---

## 💡 .env File Example (for secret key path)

```
SECRET_KEY_PATH=/etc/secrets/secret.key
```

---

## ✅ Next Steps

* Upload `common-utils` to Artifactory.
* Reference it in `ftp-scheduler` using:

  ```
  pip install common-utils
  ```
* Implement Jenkins pipeline to automate build and publish.

---

Would you also like me to give **`YES JENKINS` ready Jenkinsfile script for both build & publish to Artifactory?**
If yes, just say "`YES JENKINS FULL`".
