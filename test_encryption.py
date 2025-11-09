from encryption import generate_key, load_key, encrypt_text, decrypt_text

# Generate or load key
key = load_key()

# Sample message
msg = "This is a secret message"

# Encrypt
enc = encrypt_text(msg, key)
print("Encrypted:", enc)

# Decrypt
dec = decrypt_text(enc, key)
print("Decrypted:", dec)
