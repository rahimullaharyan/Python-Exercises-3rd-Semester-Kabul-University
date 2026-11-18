import tkinter as tk

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x350")
root.minsize(350, 300)

tk.Label(root, text="Student ID:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Department:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
department_entry = tk.Entry(root)
department_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Semester:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
semester_entry = tk.Entry(root)
semester_entry.grid(row=3, column=1, padx=10, pady=10)


def save():
    print("Student ID:", id_entry.get())
    print("Name:", name_entry.get())
    print("Department:", department_entry.get())
    print("Semester:", semester_entry.get())


def clear():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)


tk.Button(root, text="Save", command=save).grid(row=4, column=0, padx=10, pady=20)
tk.Button(root, text="Clear", command=clear).grid(row=4, column=1, padx=10, pady=20)

root.mainloop()