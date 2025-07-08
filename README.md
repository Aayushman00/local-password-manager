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
```

## 🔐 First Time Setup

When you run the tool for the first time, you’ll be prompted to create a master password. This will be hashed (not stored in plaintext) and required for all future operations.

## 🧾 Commands
### ➕ Add or Update a Password

```bash
python passman.py add <service-name>
```

### 🔑 Get a Password
```bash
python passman.py get <service-name>
```

### 🗑 Delete a Password
```bash
python passman.py delete <service-name>
```

### 📋 List All Stored Services

```bash
python passman.py list
```


## Examples

```bash
# Add password for Gmail
python passman.py add gmail

# Retrieve it
python passman.py get gmail

# Delete it
python passman.py delete gmail

# List everything
python passman.py list

```


## 🗂 File Breakdown

```bash
| File             | Description                               |
| ---------------- | ----------------------------------------- |
| `passman.py`     | Main CLI script                           |
| `passwords.json` | Stores encrypted passwords (auto-created) |
| `secret.key`     | Symmetric encryption key (auto-generated) |
| `master.hash`    | Stores master password hash (SHA-256)     |
```

## 🔄 Reset Everything (Caution)

To completely reset the manager (⚠️ all data will be lost):
```bash
del passwords.json
del secret.key
del master.hash
```
