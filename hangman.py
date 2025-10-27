# hangman.py
import random

words = ["python", "engineer", "openai", "hacktoberfest", "github"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print(" ".join(guessed))
    print(f"Attempts left: {attempts}")
    ch = input("Guess a letter: ").lower()
    if ch in word:
        for i, c in enumerate(word):
            if c == ch:
                guessed[i] = c
    else:
        attempts -= 1

if "_" not in guessed:
    print(f"🎉 You guessed it! Word: {word}")
else:
    print(f"💀 You lost! The word was: {word}")
