import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Profile Card")
root.geometry("450x500")
root.resizable(False, False)

profile_frame = tk.Frame(
    root,
    bg="white",
    padx=30,
    pady=25,
    bd=2,
    relief="groove"
)
profile_frame.pack(padx=30, pady=30, fill="both", expand=True)

image = tk.PhotoImage(file="profile.png")

image_label = tk.Label(
    profile_frame,
    image=image,
    bg="white"
)
image_label.pack(pady=10)

name_label = tk.Label(
    profile_frame,
    text="Rahimullah Aryan",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="#2C3E50"
)
name_label.pack(pady=8)

department_label = tk.Label(
    profile_frame,
    text="Department: Computer Science",
    font=("Arial", 12),
    bg="white"
)
department_label.pack(pady=5)

email_label = tk.Label(
    profile_frame,
    text="Email: aryan@example.com",
    font=("Arial", 11),
    bg="white"
)
email_label.pack(pady=5)


def edit_profile():
    messagebox.showinfo("Edit Profile", "Edit button clicked!")


def close_window():
    root.destroy()


button_frame = tk.Frame(profile_frame, bg="white")
button_frame.pack(pady=20)

edit_button = tk.Button(
    button_frame,
    text="Edit",
    font=("Arial", 11, "bold"),
    bg="#3498DB",
    fg="white",
    width=12,
    command=edit_profile
)
edit_button.pack(side="left", padx=10)

close_button = tk.Button(
    button_frame,
    text="Close",
    font=("Arial", 11, "bold"),
    bg="#E74C3C",
    fg="white",
    width=12,
    command=close_window
)
close_button.pack(side="left", padx=10)

root.mainloop()