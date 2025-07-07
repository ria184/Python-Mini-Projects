

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("450x300")
        self.root.configure(bg="#f0f8ff")  # Light blue background

        self.build_ui()

    def build_ui(self):
        # Title Label
        tk.Label(
            self.root,
            text="Password Generator",
            font=("Helvetica", 18, "bold"),
            bg="#f0f8ff",
            fg="#003366"
        ).pack(pady=15)

        # Label for instruction
        tk.Label(
            self.root,
            text="Enter desired password length:",
            font=("Helvetica", 12),
            bg="#f0f8ff"
        ).pack()

        # Entry for password length
        self.length_entry = tk.Entry(
            self.root,
            font=("Helvetica", 14),
            justify="center",
            width=8,
            relief="solid",
            bd=2
        )
        self.length_entry.pack(pady=5)

        # Generate Button
        tk.Button(
            self.root,
            text="Generate Password",
            font=("Helvetica", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            width=20,
            command=self.generate_password
        ).pack(pady=12)

        # Entry to show generated password
        self.password_entry = tk.Entry(
            self.root,
            font=("Helvetica", 14),
            justify="center",
            width=30,
            relief="ridge",
            bd=2
        )
        self.password_entry.pack(pady=8)

        # Copy to clipboard button
        tk.Button(
            self.root,
            text="Copy to Clipboard",
            font=("Helvetica", 12),
            bg="#2196F3",
            fg="white",
            activebackground="#1e88e5",
            width=20,
            command=self.copy_to_clipboard
        ).pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a number (minimum 4).")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("No Password", "Generate a password first.")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

