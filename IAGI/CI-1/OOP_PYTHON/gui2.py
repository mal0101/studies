import tkinter as tk
from tkinter import *

# Initialize the main application window
window = tk.Tk()
window.title("Text Copier and Counter")

# Variables to store text in entries
t1_text = StringVar()
t2_text = StringVar()
t3_text = StringVar()

# Define the function to copy text and count characters
def perform_action():
    # Copy text from t1 to t2
    text = t1_text.get()
    t2_text.set(text)
    
    # Count characters in t1 and display in t3
    character_count = len(text)
    t3_text.set(str(character_count))

# Define and place Entry widgets
t1_entry = tk.Entry(window, textvariable=t1_text, width=30)
t1_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Label(window, text="Entry t1:").grid(row=0, column=0, padx=10, pady=10)

t2_entry = tk.Entry(window, textvariable=t2_text, width=30)
t2_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Label(window, text="Entry t2:").grid(row=1, column=0, padx=10, pady=10)

t3_entry = tk.Entry(window, textvariable=t3_text, width=30, state="readonly")
t3_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Label(window, text="Entry t3 (Character Count):").grid(row=2, column=0, padx=10, pady=10)

# Define and place the Action button
action_button = tk.Button(window, text="Action", command=perform_action)
action_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the main event loop
window.mainloop()