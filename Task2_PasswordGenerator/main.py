import tkinter as tk
from tkinter import messagebox
from generator import generate_password

# Generate Password Function
def generate():

    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()

        password = generate_password(length, complexity)

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Copy Password Function
def copy_password():

    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )

# Show/Hide Password Function
def toggle_password():

    if password_entry.cget("show") == "*":

        password_entry.config(show="")
        show_hide_btn.config(text="Hide Password")

    else:
        password_entry.config(show="*")
        show_hide_btn.config(text="Show Password")

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x450")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=20)

# Password Length Label
length_label = tk.Label(
    root,
    text="Enter Password Length",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

length_label.pack()

# Length Entry
length_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

length_entry.pack(pady=10)

# Complexity Label
complexity_label = tk.Label(
    root,
    text="Select Password Complexity",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

complexity_label.pack(pady=5)

# Complexity Variable
complexity_var = tk.StringVar(value="3")

# Radio Buttons
radio1 = tk.Radiobutton(
    root,
    text="Lowercase Only",
    variable=complexity_var,
    value="1",
    bg="#1e1e1e",
    fg="white",
    selectcolor="#2d2d2d",
    font=("Arial", 10)
)

radio1.pack()

radio2 = tk.Radiobutton(
    root,
    text="Letters + Numbers",
    variable=complexity_var,
    value="2",
    bg="#1e1e1e",
    fg="white",
    selectcolor="#2d2d2d",
    font=("Arial", 10)
)

radio2.pack()

radio3 = tk.Radiobutton(
    root,
    text="Letters + Numbers + Symbols",
    variable=complexity_var,
    value="3",
    bg="#1e1e1e",
    fg="white",
    selectcolor="#2d2d2d",
    font=("Arial", 10)
)

radio3.pack()

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    width=22
)

generate_btn.pack(pady=20)

# Password Entry
password_entry = tk.Entry(
    root,
    font=("Arial", 13, "bold"),
    width=30,
    justify="center",
    bg="#2d2d2d",
    fg="#009DFF",
    insertbackground="white",
    show="*",
    readonlybackground="#2d2d2d",
    selectbackground="#444444",
    selectforeground="white"
)

password_entry.pack(pady=10)

# Show/Hide Button
show_hide_btn = tk.Button(
    root,
    text="Show Password",
    command=toggle_password,
    bg="#FF9800",
    fg="white",
    font=("Arial", 10, "bold"),
    width=18
)

show_hide_btn.pack(pady=5)

# Copy Button
copy_btn = tk.Button(
    root,
    text="Copy to Clipboard",
    command=copy_password,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    width=22
)

copy_btn.pack(pady=15)

# Run Application
root.mainloop()