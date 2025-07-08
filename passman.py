import os
import json
import argparse
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass
import pyperclip

DB_FILE = 'passwords.json'
KEY_FILE = 'secret.key'
MASTER_HASH_FILE = 'master.hash'

def create_master_password():
    print("🔐 First-time setup: Create a master password.")
    pwd = getpass("Enter master password: ")
    confirm = getpass("Confirm master password: ")
    if pwd != confirm:
        print("Passwords do not match.")
        exit(1)
    hashed = hashlib.sha256(pwd.encode()).hexdigest()
    with open(MASTER_HASH_FILE, 'w') as f:
        f.write(hashed)
    print("Master password set. Keep it safe!")

def verify_master_password():
    if not os.path.exists(MASTER_HASH_FILE):
        create_master_password()
    pwd = getpass("Enter master password to unlock: ")
    hashed_input = hashlib.sha256(pwd.encode()).hexdigest()
    with open(MASTER_HASH_FILE, 'r') as f:
        saved_hash = f.read()
    if hashed_input != saved_hash:
        print("❌ Incorrect master password.")
        exit(1)

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_password(service, password):
    key = load_key()
    fernet = Fernet(key)
    data = load_data()
    encrypted = fernet.encrypt(password.encode()).decode()
    data[service] = encrypted
    save_data(data)
    print(f"✅ Password for '{service}' saved.")

def get_password(service):
    key = load_key()
    fernet = Fernet(key)
    data = load_data()
    if service in data:
        decrypted = fernet.decrypt(data[service].encode()).decode()
        pyperclip.copy(decrypted)
        print(f"📋 Password for '{service}' copied to clipboard.")
    else:
        print(f"❌ No password found for '{service}'.")

def delete_password(service):
    data = load_data()
    if service in data:
        del data[service]
        save_data(data)
        print(f"🗑️ Password for '{service}' deleted.")
    else:
        print(f"❌ No password found for '{service}'.")

def list_services():
    data = load_data()
    if data:
        print("📦 Stored services:")
        for service in data:
            print(f" - {service}")
    else:
        print("📭 No passwords stored yet.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='🔐 Secure CLI Password Manager')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add or update a password')
    add_parser.add_argument('service', help='Service name')

    get_parser = subparsers.add_parser('get', help='Retrieve a password')
    get_parser.add_argument('service', help='Service name')

    delete_parser = subparsers.add_parser('delete', help='Delete a password')
    delete_parser.add_argument('service', help='Service name')

    list_parser = subparsers.add_parser('list', help='List all stored services')

    args = parser.parse_args()

    verify_master_password()

    if args.command == 'add':
        pwd = getpass(f"Enter password for '{args.service}': ")
        add_password(args.service, pwd)

    elif args.command == 'get':
        get_password(args.service)

    elif args.command == 'delete':
        delete_password(args.service)

    elif args.command == 'list':
        list_services()

    else:
        parser.print_help()
