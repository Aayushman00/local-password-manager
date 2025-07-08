# 🔐 CLI Password Manager

A simple, secure local password manager built with Python. It stores encrypted passwords using Fernet, is protected by a master password, and supports clipboard copy for quick retrieval.

---

## Features

- 💾 Local storage (no cloud, no sync, no leaks)
- 🔐 Master password protection (hashed, not stored)
- 🔒 AES-128 encryption via Fernet (symmetric key)
- 📋 Clipboard copy on retrieval
- 📦 Add, retrieve, delete, and list passwords

---

## Getting Started

### 1. Install Requirements

```bash
pip install cryptography pyperclip
