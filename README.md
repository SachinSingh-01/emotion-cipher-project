# Emotion Cipher

Hey there!  
This is my small Python project for the Emotion Cipher hackathon hosted on Unstop.

I built this to understand how emotions can be detected from text and how we can encrypt messages while keeping their emotional meaning safe.

### What It Does
- Takes a sentence from the user.
- Detects its emotion (like joy, anger, sadness, anxiety, etc.).
- Encrypts the original text using Python’s cryptography library.
- Decrypts it back when needed.

### Example
Input → "I'm excited to join my new team, but also nervous about the first day!"  
Detected Emotion → Joy + Anxiety  
Encrypted → gAAAAAB...  
Decrypted → original message again 

### How to Run
1. Install required package:
