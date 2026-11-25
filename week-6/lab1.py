import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Information Form")
root.geometry("500x550")
root.resizable(False, False)

header_frame = tk.Frame(root, bg="#2C3E50", pady=20)
header_frame.pack(fill="x")

title = tk.Label(
    header_frame,
    text="Student Information Form",
    font=("Arial", 18, "bold"),
    bg="#2C3E50",
    fg="white"
)
title.pack()

form_frame = tk.Frame(root, padx=30, pady=20)
form_frame.pack(fill="both", expand=True)

tk.Label(form_frame, text="Full Name:").grid(row=0, column=0, sticky="w", pady=10)
name_entry = tk.Entry(form_frame, width=35)
name_entry.grid(row=0, column=1, pady=10)

tk.Label(form_frame, text="Student ID:").grid(row=1, column=0, sticky="w", pady=10)
id_entry = tk.Entry(form_frame, width=35)
id_entry.grid(row=1, column=1, pady=10)

tk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky="w", pady=10)
email_entry = tk.Entry(form_frame, width=35)
email_entry.grid(row=2, column=1, pady=10)

tk.Label(form_frame, text="Phone:").grid(row=3, column=0, sticky="w", pady=10)
phone_entry = tk.Entry(form_frame, width=35)
phone_entry.grid(row=3, column=1, pady=10)

tk.Label(form_frame, text="Address:").grid(row=4, column=0, sticky="nw", pady=10)
address_text = tk.Text(form_frame, width=26, height=5)
address_text.grid(row=4, column=1, pady=10)

actions_frame = tk.Frame(root, pady=15)
actions_frame.pack()

status_label = tk.Label(root, text="Ready", fg="gray", font=("Arial", 10))
status_label.pack(pady=10)


def save_data():
    name = name_entry.get()
    student_id = id_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_text.get("1.0", tk.END).strip()

    if not name or not student_id or not email or not phone or not address:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        status_label.config(text="Please complete all fields.", fg="red")
    else:
        status_label.config(text="Student information saved successfully!", fg="green")
        messagebox.showinfo("Success", "Student information saved successfully!")


def clear_fields():
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)
    status_label.config(text="Form cleared.", fg="blue")


save_button = tk.Button(
    actions_frame,
    text="Save",
    width=12,
    bg="green",
    fg="white",
    command=save_data
)
save_button.pack(side="left", padx=10)

clear_button = tk.Button(
    actions_frame,
    text="Clear",
    width=12,
    bg="red",
    fg="white",
    command=clear_fields
)
clear_button.pack(side="left", padx=10)

root.mainloop()