# Emotion Cipher

A small Python prototype that combines **keyword-based emotion detection** with **Fernet encryption and decryption**. The project was created as an Emotion Cipher hackathon project hosted on Unstop.

The application takes a text message, detects matching emotions using a predefined set of keywords, encrypts the message, and then decrypts it again to demonstrate the complete workflow.

> **Project scope:** This is a simple prototype. Emotion detection is based on keyword matching and is not a machine-learning or advanced NLP model.

## What the Project Does

### 1. Emotion Detection

The `emotion_detection.py` module checks the user's message against predefined keywords.

Supported emotions:

- **Joy** — happy, joy, excited, thrilled, glad
- **Sadness** — sad, disappointed, unhappy, depressed
- **Anger** — angry, mad, frustrated, annoyed
- **Fear** — worried, afraid, scared, nervous
- **Surprise** — surprised, shocked, amazed
- **Love** — love, affection, caring
- **Neutral** — returned when no configured emotion keyword is detected

Multiple emotions can be detected in the same message.

Example:

```text
Input:
I am so happy and excited today!

Detected:
Joy
```

### 2. Encryption and Decryption

The `encryption.py` module uses **Fernet** from the Python `cryptography` package.

It provides functions to:

- Generate an encryption key
- Load an existing key
- Encrypt text
- Decrypt encrypted text

The encryption key is stored locally in `key.key`. The repository's `.gitignore` excludes this file so the secret key is not committed to Git.

## Application Flow

The integrated workflow in `main.py` is:

```text
User enters a message
        ↓
Check for empty input
        ↓
Load or generate encryption key
        ↓
Detect emotions using keywords
        ↓
Encrypt the original message
        ↓
Decrypt the encrypted message
        ↓
Display original message, emotions,
encrypted message, and decrypted message
```

## Project Structure

```text
emotion-cipher-project/
│
├── emotion_detection.py    # Keyword-based emotion detection
├── encryption.py            # Fernet encryption/decryption
├── main.py                  # Integrated command-line application
├── test_emotion.py          # Basic emotion detection test
├── test_encryption.py       # Basic encryption/decryption test
├── requirements.txt         # Python dependency
├── .gitignore               # Ignores local secrets and generated files
├── README.md
└── VID20251109145253 (1) (1).mp4
```

## Requirements

- Python 3
- `cryptography`

The required Python package is listed in `requirements.txt`.

## Installation

Clone the repository and install the dependency:

```bash
pip install -r requirements.txt
```

## Run the Project

Run the integrated application:

```bash
python main.py
```

You will be asked to enter a message.

The application then displays:

- Original message
- Detected emotion(s)
- Encrypted message
- Decrypted message

If `key.key` does not exist, the application generates a new Fernet key automatically.

## Run the Tests

### Emotion detection

```bash
python test_emotion.py
```

### Encryption and decryption

```bash
python test_encryption.py
```

These are simple executable test scripts that demonstrate the corresponding functionality.

## Security Notes

The project uses Fernet symmetric encryption, meaning the same secret key is required for encryption and decryption.

The local `key.key` file contains the secret encryption key and is included in `.gitignore`. **Do not commit or share this key in a real application.**

This project is intended for learning and demonstration purposes. It is not presented as a production-grade secure messaging system.

## Limitations

### Emotion Detection

Emotion detection is implemented with straightforward keyword matching. Therefore:

- It does not understand context or sentence meaning.
- It can miss emotions expressed without the configured keywords.
- A keyword appearing in a different context may still trigger an emotion.
- It does not use machine learning, deep learning, or a trained NLP model.

### Encryption

The project demonstrates text encryption and decryption locally. It does not implement a complete messaging system, key exchange protocol, authentication system, or secure network communication layer.

## Technologies Used

- **Python**
- **Cryptography**
- **Fernet symmetric encryption**

## Author

**Sachin Kumar**

Built as a Python project for the Emotion Cipher hackathon.

GitHub: [SachinSingh-01](https://github.com/SachinSingh-01)
