# 🔐 CLI Password Manager

A simple, secure local password manager built in Python. It stores encrypted passwords locally using Fernet (AES-based symmetric encryption), protects access with a master password, and copies passwords to your clipboard securely — nothing printed to the screen.

---

## 🚀 Features

- 💾 Fully local storage (`passwords.json`)
- 🔐 Master password protection (stored as SHA-256 hash)
- 🔒 Encryption via Fernet (AES-128 under the hood)
- 📋 Clipboard copy for password retrieval
- 📦 Commands to add, get, delete, and list services
- 🧪 Minimal dependencies, quick setup

---

## 📦 Requirements

- Python 3.7+
- Libraries:
  - `cryptography`
  - `pyperclip`

### 🔧 Install Dependencies

Install manually:

```bash
pip install cryptography pyperclip
