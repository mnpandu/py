# saas_secrets

🔐 A secure and reusable Python utility for managing encrypted secrets (like database passwords) using Fernet encryption. Built for SaaS teams transitioning from hardcoded secrets or SaaS-config storage to Python-based deployments.

## Features

- Encrypt and decrypt secrets using `cryptography.fernet`
- Store encrypted secrets in `.env` or config files
- Centralized key management using `secret.key` in the app root
- Simple integration with any Python app or microservice

## Installation

Install from your Artifactory private PyPI repo:

```bash
pip install saas_secrets --extra-index-url https://<your-artifactory-url>/artifactory/api/pypi/<your-pypi-repo>/simple
