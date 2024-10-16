import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


# Function to generate a password
def generate_password():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        if length <= 0:
            raise ValueError

        character_set = ""
        if use_letters:
            character_set += string.ascii_letters
        if use_numbers:
            character_set += string.digits
        if use_symbols:
            character_set += string.punctuation

        if not character_set:
            messagebox.showerror("Selection Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(character_set) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")


# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Clipboard", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "No password to copy. Please generate a password first.")


# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Frame for password length
tk.Label(app, text="Password Length:").grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Checkboxes for character types
letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(app, text="Include Letters", variable=letters_var).grid(row=1, column=0, columnspan=2, padx=10, pady=5)
tk.Checkbutton(app, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, columnspan=2, padx=10, pady=5)
tk.Checkbutton(app, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Entry for displaying generated password
password_entry = tk.Entry(app, width=30)
password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Buttons for generating password and copying to clipboard
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, padx=10, pady=5)

copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=5, column=1, padx=10, pady=5)

# Start the Tkinter event loop
app.mainloop()