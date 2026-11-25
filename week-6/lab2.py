import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("650x500")
root.minsize(400, 300)

header_frame = tk.Frame(root, bg="#2C3E50", pady=15)
header_frame.pack(fill="x")

title_label = tk.Label(
    header_frame,
    text="My Text Editor",
    font=("Arial", 20, "bold"),
    bg="#2C3E50",
    fg="white"
)
title_label.pack()

editor_frame = tk.Frame(root, padx=15, pady=15)
editor_frame.pack(fill="both", expand=True)

text_editor = tk.Text(editor_frame, font=("Arial", 12), wrap="word")
text_editor.pack(fill="both", expand=True)

action_frame = tk.Frame(root, pady=10)
action_frame.pack(fill="x")

status_label = tk.Label(root, text="Ready", fg="green")
status_label.pack(pady=5)


def clear_text():
    text_editor.delete("1.0", tk.END)
    status_label.config(text="Editor cleared.", fg="blue")


def insert_sample():
    sample = "Welcome to Python Tkinter!\n\nThis is a simple text editor.\nYou can write, edit, save, and load your notes."
    text_editor.delete("1.0", tk.END)
    text_editor.insert("1.0", sample)
    status_label.config(text="Sample text inserted.", fg="green")


def toggle_editor():
    if text_editor.cget("state") == "normal":
        text_editor.config(state="disabled")
        toggle_button.config(text="Enable")
        status_label.config(text="Editor disabled.", fg="red")
    else:
        text_editor.config(state="normal")
        toggle_button.config(text="Disable")
        status_label.config(text="Editor enabled.", fg="green")


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        content = text_editor.get("1.0", tk.END)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        status_label.config(text="File saved successfully.", fg="green")


def load_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        text_editor.config(state="normal")
        text_editor.delete("1.0", tk.END)
        text_editor.insert("1.0", content)

        status_label.config(text="File loaded successfully.", fg="green")
        toggle_button.config(text="Disable")


clear_button = tk.Button(
    action_frame,
    text="Clear",
    width=12,
    command=clear_text
)
clear_button.pack(side="left", padx=5)

sample_button = tk.Button(
    action_frame,
    text="Insert Sample Text",
    width=16,
    command=insert_sample
)
sample_button.pack(side="left", padx=5)

toggle_button = tk.Button(
    action_frame,
    text="Disable",
    width=12,
    command=toggle_editor
)
toggle_button.pack(side="left", padx=5)

save_button = tk.Button(
    action_frame,
    text="Save",
    width=10,
    command=save_file
)
save_button.pack(side="left", padx=5)

load_button = tk.Button(
    action_frame,
    text="Load",
    width=10,
    command=load_file
)
load_button.pack(side="left", padx=5)

root.mainloop()
