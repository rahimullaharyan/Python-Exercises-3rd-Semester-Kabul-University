import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Registration System")
root.geometry("700x700")
root.minsize(550, 600)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

header_frame = tk.Frame(root, bg="#2C3E50", pady=20)
header_frame.grid(row=0, column=0, sticky="ew")

title_label = tk.Label(
    header_frame,
    text="Student Registration System",
    font=("Arial", 20, "bold"),
    bg="#2C3E50",
    fg="white"
)
title_label.pack()

main_frame = tk.Frame(root, padx=25, pady=15)
main_frame.grid(row=1, column=0, sticky="nsew")

main_frame.columnconfigure(1, weight=1)

personal_frame = tk.LabelFrame(
    main_frame,
    text="Personal Information",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=10
)
personal_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

personal_frame.columnconfigure(1, weight=1)

tk.Label(personal_frame, text="Student ID:").grid(row=0, column=0, sticky="w", pady=8)
id_entry = tk.Entry(personal_frame)
id_entry.grid(row=0, column=1, sticky="ew", pady=8)

tk.Label(personal_frame, text="Full Name:").grid(row=1, column=0, sticky="w", pady=8)
name_entry = tk.Entry(personal_frame)
name_entry.grid(row=1, column=1, sticky="ew", pady=8)

tk.Label(personal_frame, text="Email:").grid(row=2, column=0, sticky="w", pady=8)
email_entry = tk.Entry(personal_frame)
email_entry.grid(row=2, column=1, sticky="ew", pady=8)

tk.Label(personal_frame, text="Phone:").grid(row=3, column=0, sticky="w", pady=8)
phone_entry = tk.Entry(personal_frame)
phone_entry.grid(row=3, column=1, sticky="ew", pady=8)

academic_frame = tk.LabelFrame(
    main_frame,
    text="Academic Information",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=10
)
academic_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

academic_frame.columnconfigure(1, weight=1)

tk.Label(academic_frame, text="Department:").grid(row=0, column=0, sticky="w", pady=8)

department_var = tk.StringVar()

department_menu = tk.OptionMenu(
    academic_frame,
    department_var,
    "Computer Science",
    "Information Technology",
    "Software Engineering",
    "Information Systems"
)
department_menu.grid(row=0, column=1, sticky="ew", pady=8)

tk.Label(academic_frame, text="Semester:").grid(row=1, column=0, sticky="w", pady=8)

semester_var = tk.StringVar()

semester_menu = tk.OptionMenu(
    academic_frame,
    semester_var,
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8"
)
semester_menu.grid(row=1, column=1, sticky="ew", pady=8)

notes_frame = tk.LabelFrame(
    main_frame,
    text="Additional Notes",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=10
)
notes_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)

notes_frame.columnconfigure(0, weight=1)

notes_text = tk.Text(notes_frame, height=4, wrap="word")
notes_text.grid(row=0, column=0, sticky="ew")

action_frame = tk.Frame(main_frame, pady=15)
action_frame.grid(row=3, column=0, columnspan=2)

status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 10),
    fg="gray",
    pady=10
)
status_label.grid(row=2, column=0, sticky="ew")


def save_data():
    student_id = id_entry.get().strip()
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    department = department_var.get()
    semester = semester_var.get()
    notes = notes_text.get("1.0", tk.END).strip()

    if not student_id or not name or not email or not phone:
        status_label.config(text="Please fill in all personal fields.", fg="red")
        messagebox.showwarning("Missing Information", "Please complete all personal fields.")
        return

    if "@" not in email or "." not in email:
        status_label.config(text="Please enter a valid email.", fg="red")
        messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
        return

    if not department or not semester:
        status_label.config(text="Please complete academic information.", fg="red")
        messagebox.showwarning("Missing Information", "Select department and semester.")
        return

    record = (
        f"Student ID: {student_id}\n"
        f"Full Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Department: {department}\n"
        f"Semester: {semester}\n"
        f"Notes: {notes}\n"
        f"{'-' * 40}\n"
    )

    try:
        with open("students.txt", "a", encoding="utf-8") as file:
            file.write(record)

        status_label.config(text="Student registered successfully!", fg="green")
        messagebox.showinfo("Success", "Student information saved successfully!")

    except OSError:
        status_label.config(text="Error saving student information.", fg="red")
        messagebox.showerror("Error", "Could not save the student record.")


def clear_fields():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    department_var.set("")
    semester_var.set("")
    notes_text.delete("1.0", tk.END)

    status_label.config(text="All fields cleared.", fg="blue")


def exit_program():
    root.destroy()


save_button = tk.Button(
    action_frame,
    text="Save",
    width=12,
    bg="#27AE60",
    fg="white",
    font=("Arial", 10, "bold"),
    command=save_data
)
save_button.pack(side="left", padx=8)

clear_button = tk.Button(
    action_frame,
    text="Clear",
    width=12,
    bg="#F39C12",
    fg="white",
    font=("Arial", 10, "bold"),
    command=clear_fields
)
clear_button.pack(side="left", padx=8)

exit_button = tk.Button(
    action_frame,
    text="Exit",
    width=12,
    bg="#C0392B",
    fg="white",
    font=("Arial", 10, "bold"),
    command=exit_program
)
exit_button.pack(side="left", padx=8)

root.mainloop()