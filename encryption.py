# encryption.py
# Simple encryption + decryption utility using Fernet.
# I kept it minimal so it’s easy to read and test.

from cryptography.fernet import Fernet
import os

def generate_key(file_name="key.key"):
    """Generates a new secret key and saves it to a file."""
    key = Fernet.generate_key()
    with open(file_name, "wb") as f:
        f.write(key)
    print("New encryption key generated successfully.")
    return key

def load_key(file_name="key.key"):
    """Loads existing key if available, otherwise creates one."""
    if not os.path.exists(file_name):
        print("Key not found, creating a new one...")
        return generate_key(file_name)
    with open(file_name, "rb") as f:
        return f.read()

def encrypt_text(text, key):
    """Encrypts plain text using the given key."""
    cipher = Fernet(key)
    token = cipher.encrypt(text.encode())
    return token.decode()

def decrypt_text(token, key):
    """Decrypts cipher text back to plain text."""
    cipher = Fernet(key)
    decoded = cipher.decrypt(token.encode())
    return decoded.decode()
