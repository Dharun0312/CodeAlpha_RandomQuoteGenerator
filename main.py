import tkinter as tk
import random

quotes = [
    ("Believe in yourself!", "Unknown"),
    ("Never give up on your dreams.", "Unknown"),
    ("Success is the result of hard work.", "Unknown"),
    ("Every day is a new beginning.", "Unknown"),
    ("Dream big and work hard.", "Unknown")
]

def generate_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=quote)
    author_label.config(text="- " + author)

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("500x300")
root.configure(bg="#20232A")

title = tk.Label(
    root, text="Random Quote Generator",
    font=("Arial", 20, "bold"),
    bg="#20232A", fg="white"
)
title.pack(pady=25)

quote_label = tk.Label(
    root, text="Click below to get a quote",
    font=("Arial", 14),
    bg="#20232A", fg="white",
    wraplength=400
)
quote_label.pack(pady=20)

author_label = tk.Label(
    root, text="",
    font=("Arial", 12, "italic"),
    bg="#20232A", fg="orange"
)
author_label.pack()

button = tk.Button(
    root, text="New Quote",
    command=generate_quote,
    font=("Arial", 12, "bold"),
    bg="orange", fg="black"
)
button.pack(pady=25)

generate_quote()
root.mainloop()