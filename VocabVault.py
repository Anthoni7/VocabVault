import tkinter as tk
from tkinter import messagebox
import json
import random
import pyttsx3


# Load words from the JSON file
def load_words():
    try:
        with open("C:\\Users\\HP\\Desktop\\MY LF\\Python Programming\\EngDict.json", "r") as file:  # Update the file path
            data = json.load(file)
            return data["word"]  # Return the dictionary of words
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load words: {e}")
        return {}


# Function to pick a random word
def get_random_word():
    if words:
        random_word = random.choice(list(words.keys()))  # Select a random word key
        return random_word, words[random_word]  # Return the word and its details
    else:
        messagebox.showerror("Error", "No words available!")
        return None, None


# Function to pronounce the word
def pronounce_word(word):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # Get the current speech rate
    engine.setProperty('rate', rate - 50)  # Reduce the rate by 50 (or set a specific value like 150)
    engine.say(word)
    engine.runAndWait()


# Function to generate a new word and display details
def generate_word():
    word, details = get_random_word()
    if word:
        word_label.config(text=f"Word: {word}")
        meaning_label.config(text=f"Meaning: {details['meaning']}")
        pronunciation_label.config(text=f"Pronunciation: {details['pronunciation']}")
        pronounce_button.config(state=tk.NORMAL)
    else:
        word_label.config(text="Word: -")
        meaning_label.config(text="Meaning: -")
        pronunciation_label.config(text="Pronunciation: -")
        pronounce_button.config(state=tk.DISABLED)


# Load words from EngDict.json file
words = load_words()

# Create the main app window
app = tk.Tk()
app.title("Offline Word Generator")
app.geometry("400x300")

# UI Components
title_label = tk.Label(app, text="Offline Word Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

word_label = tk.Label(app, text="Word: -", font=("Helvetica", 14))
word_label.pack(pady=5)

meaning_label = tk.Label(app, text="Meaning: -", wraplength=380, font=("Helvetica", 12))
meaning_label.pack(pady=5)

pronunciation_label = tk.Label(app, text="Pronunciation: -", font=("Helvetica", 12))
pronunciation_label.pack(pady=5)

generate_button = tk.Button(app, text="Generate Word", command=generate_word)
generate_button.pack(pady=10)

pronounce_button = tk.Button(app, text="Pronounce Word", command=lambda: pronounce_word(word_label.cget("text").split(": ")[1]), state=tk.DISABLED)
pronounce_button.pack(pady=10)

# Run the app
app.mainloop()
