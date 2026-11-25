import tkinter as tk
from tkinter import messagebox


class PersonalInformationForm:

    def __init__(self, root):
        self.root = root
        self.root.title("Personal Information Form")
        self.root.geometry("550x500")
        self.root.minsize(450, 450)

        self.create_header()
        self.create_form()
        self.create_footer()

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="lightblue")
        header_frame.pack(fill="x")

        heading = tk.Label(
            header_frame,
            text="Personal Information Form",
            font=("Arial", 20, "bold"),
            bg="lightblue"
        )
        heading.pack(pady=20)

    def create_form(self):
        self.form_frame = tk.Frame(self.root, padx=30, pady=20)
        self.form_frame.pack(fill="both", expand=True)

        self.form_frame.columnconfigure(1, weight=1)

        self.entries = {}

        fields = [
            "Full Name",
            "Student ID",
            "Email",
            "Department",
            "Semester",
            "Phone"
        ]

        for row, field in enumerate(fields):
            label = tk.Label(self.form_frame, text=field + ":")
            label.grid(row=row, column=0, padx=10, pady=10, sticky="w")

            entry = tk.Entry(self.form_frame)
            entry.grid(row=row, column=1, padx=10, pady=10, sticky="ew")

            self.entries[field] = entry

    def create_footer(self):
        footer_frame = tk.Frame(self.root)
        footer_frame.pack(fill="x", pady=15)

        save_button = tk.Button(
            footer_frame,
            text="Save",
            width=12,
            command=self.save_information
        )
        save_button.pack(side="left", padx=40)

        clear_button = tk.Button(
            footer_frame,
            text="Clear",
            width=12,
            command=self.clear_information
        )
        clear_button.pack(side="left", padx=20)

        exit_button = tk.Button(
            footer_frame,
            text="Exit",
            width=12,
            command=self.root.destroy
        )
        exit_button.pack(side="left", padx=20)

    def save_information(self):
        print("\n--- Personal Information ---")

        for field, entry in self.entries.items():
            print(field + ":", entry.get())

        messagebox.showinfo("Success", "Information saved successfully!")

    def clear_information(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)


root = tk.Tk()
app = PersonalInformationForm(root)
root.mainloop()