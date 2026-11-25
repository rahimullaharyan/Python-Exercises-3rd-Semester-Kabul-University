import tkinter as tk
from tkinter import messagebox
import csv
import os

root = tk.Tk()
root.title("Employee Registration System")
root.geometry("750x750")
root.minsize(550, 600)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

header_frame = tk.Frame(root, bg="#2C3E50", pady=15)
header_frame.grid(row=0, column=0, sticky="ew")

header_frame.columnconfigure(1, weight=1)

logo = tk.PhotoImage(file="logo.png")

logo_label = tk.Label(
    header_frame,
    image=logo,
    bg="#2C3E50"
)
logo_label.grid(row=0, column=0, padx=20)

title_label = tk.Label(
    header_frame,
    text="Employee Registration System",
    font=("Arial", 20, "bold"),
    bg="#2C3E50",
    fg="white"
)
title_label.grid(row=0, column=1, sticky="w")

form_frame = tk.LabelFrame(
    root,
    text="Employee Information",
    font=("Arial", 12, "bold"),
    padx=25,
    pady=20
)
form_frame.grid(row=1, column=0, padx=30, pady=20, sticky="nsew")

form_frame.columnconfigure(1, weight=1)
form_frame.rowconfigure(5, weight=1)

tk.Label(form_frame, text="Employee ID:", font=("Arial", 11)).grid(
    row=0, column=0, sticky="w", pady=12
)
id_entry = tk.Entry(form_frame, font=("Arial", 11))
id_entry.grid(row=0, column=1, sticky="ew", pady=12)

tk.Label(form_frame, text="Full Name:", font=("Arial", 11)).grid(
    row=1, column=0, sticky="w", pady=12
)
name_entry = tk.Entry(form_frame, font=("Arial", 11))
name_entry.grid(row=1, column=1, sticky="ew", pady=12)

tk.Label(form_frame, text="Email:", font=("Arial", 11)).grid(
    row=2, column=0, sticky="w", pady=12
)
email_entry = tk.Entry(form_frame, font=("Arial", 11))
email_entry.grid(row=2, column=1, sticky="ew", pady=12)

tk.Label(form_frame, text="Phone:", font=("Arial", 11)).grid(
    row=3, column=0, sticky="w", pady=12
)
phone_entry = tk.Entry(form_frame, font=("Arial", 11))
phone_entry.grid(row=3, column=1, sticky="ew", pady=12)

tk.Label(form_frame, text="Position:", font=("Arial", 11)).grid(
    row=4, column=0, sticky="w", pady=12
)
position_entry = tk.Entry(form_frame, font=("Arial", 11))
position_entry.grid(row=4, column=1, sticky="ew", pady=12)

tk.Label(form_frame, text="Address:", font=("Arial", 11)).grid(
    row=5, column=0, sticky="nw", pady=12
)
address_text = tk.Text(form_frame, height=5, font=("Arial", 11), wrap="word")
address_text.grid(row=5, column=1, sticky="nsew", pady=12)

actions_frame = tk.Frame(root, pady=15)
actions_frame.grid(row=2, column=0, sticky="ew")

status_frame = tk.Frame(root, bg="#ECF0F1", pady=12)
status_frame.grid(row=3, column=0, sticky="ew")

status_label = tk.Label(
    status_frame,
    text="Ready to register an employee.",
    font=("Arial", 10, "italic"),
    bg="#ECF0F1",
    fg="gray"
)
status_label.pack()


def save_employee():
    employee_id = id_entry.get().strip()
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    position = position_entry.get().strip()
    address = address_text.get("1.0", tk.END).strip()

    if not all([employee_id, name, email, phone, position, address]):
        status_label.config(
            text="Please fill in all required fields.",
            fg="red"
        )
        messagebox.showwarning(
            "Missing Information",
            "All fields are required."
        )
        return

    if "@" not in email or "." not in email:
        status_label.config(text="Invalid email address.", fg="red")
        messagebox.showwarning("Invalid Email", "Please enter a valid email.")
        return

    employee = [
        employee_id,
        name,
        email,
        phone,
        position,
        address
    ]

    file_exists = os.path.isfile("employees.csv")

    try:
        with open("employees.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists or os.path.getsize("employees.csv") == 0:
                writer.writerow([
                    "Employee ID",
                    "Name",
                    "Email",
                    "Phone",
                    "Position",
                    "Address"
                ])

            writer.writerow(employee)

        status_label.config(
            text="Employee registered successfully!",
            fg="green"
        )

        messagebox.showinfo(
            "Success",
            "Employee information saved successfully!"
        )

    except OSError:
        status_label.config(
            text="Unable to save employee information.",
            fg="red"
        )
        messagebox.showerror("Error", "Could not save the employee record.")


def clear_fields():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)

    status_label.config(
        text="All fields cleared.",
        fg="blue"
    )


def exit_program():
    root.destroy()


save_button = tk.Button(
    actions_frame,
    text="Save",
    width=15,
    font=("Arial", 10, "bold"),
    bg="#27AE60",
    fg="white",
    command=save_employee
)
save_button.pack(side="left", padx=15)

clear_button = tk.Button(
    actions_frame,
    text="Clear",
    width=15,
    font=("Arial", 10, "bold"),
    bg="#F39C12",
    fg="white",
    command=clear_fields
)
clear_button.pack(side="left", padx=15)

exit_button = tk.Button(
    actions_frame,
    text="Exit",
    width=15,
    font=("Arial", 10, "bold"),
    bg="#C0392B",
    fg="white",
    command=exit_program
)
exit_button.pack(side="left", padx=15)

root.mainloop()