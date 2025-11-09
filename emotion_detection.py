# Author: Sachin Kumar
# Date: 9 November 2025

# emotion_detection.py
# My own simple logic for detecting emotions from text.
# It’s not perfect, but it works well for small prototypes.

EMOTION_KEYWORDS = {
    "Joy": ["happy", "joy", "excited", "thrilled", "glad"],
    "Sadness": ["sad", "disappointed", "unhappy", "depressed"],
    "Anger": ["angry", "mad", "frustrated", "annoyed"],
    "Fear": ["worried", "afraid", "scared", "nervous"],
    "Surprise": ["surprised", "shocked", "amazed"],
    "Love": ["love", "affection", "caring"]
}

def detect_emotions(text):
    """Detects emotions from a sentence based on simple keywords."""
    text = text.lower()
    found = []

    for emotion, words in EMOTION_KEYWORDS.items():
        for w in words:
            if w in text:
                found.append(emotion)
                break  # avoid duplicates if many words match

    if not found:
        found = ["Neutral"]

    return found
