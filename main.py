# main.py
# -------------------------------------------------------------
# Emotion Cipher - Final Integrated Project
# Author: Sachin Kumar
# Date: November 2025
#
# This file combines:
# 1. Emotion detection (keyword-based)
# 2. Encryption & Decryption using Fernet
# -------------------------------------------------------------

from emotion_detection import detect_emotions
from encryption import load_key, generate_key, encrypt_text, decrypt_text
import os

def ensure_key():
    """Checks if encryption key exists; creates one if not."""
    key_file = "key.key"
    if not os.path.exists(key_file):
        print("[*] No key found, generating new key...")
        generate_key(key_file)
    return load_key(key_file)

def main():
    print("\n==============================")
    print("🧠 Emotion Cipher - Python Project")
    print("==============================\n")

    # Step 1 — Load or generate encryption key
    key = ensure_key()

    # Step 2 — Take user input message
    message = input("Enter your message: ").strip()
    if not message:
        print("[!] Empty message entered. Exiting...")
        return

    # Step 3 — Detect emotion(s)
    emotions = detect_emotions(message)

    # Step 4 — Encrypt the message
    encrypted_msg = encrypt_text(message, key)

    # Step 5 — Decrypt back for demo purpose
    decrypted_msg = decrypt_text(encrypted_msg, key)

    # Step 6 — Show Results
    print("\n---------- OUTPUT ----------")
    print(f"Original Message: {message}")
    print(f"Detected Emotions: {', '.join(emotions)}")
    print(f"Encrypted Message: {encrypted_msg}")
    print(f"Decrypted Message: {decrypted_msg}")
    print("----------------------------\n")

if __name__ == "__main__":
    main()
