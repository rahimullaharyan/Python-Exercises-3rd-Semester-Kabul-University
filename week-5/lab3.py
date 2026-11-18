import tkinter as tk

root = tk.Tk()
root.title("Nested Frames Layout")
root.geometry("500x400")
root.minsize(350, 300)

header = tk.Frame(root, bg="lightblue", height=60)
header.pack(fill="x")

tk.Label(header, text="Student Information", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=15)

content = tk.Frame(root, padx=20, pady=20)
content.pack(fill="both", expand=True)

content.columnconfigure(1, weight=1)

tk.Label(content, text="Student ID:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
id_entry = tk.Entry(content)
id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(content, text="Name:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(content)
name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

tk.Label(content, text="Department:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
department_entry = tk.Entry(content)
department_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

footer = tk.Frame(root, bg="lightgray", height=50)
footer.pack(fill="x")

tk.Button(footer, text="Save").pack(pady=10)

root.mainloop()