import tkinter as tk

root = tk.Tk()
root.title("Advanced Programming Lab")
root.geometry("500x350")
root.minsize(400, 300)

heading = tk.Label(root, text="Advanced Programming Lab", font=("Arial", 18, "bold"))
heading.pack(pady=20)

button1 = tk.Button(root, text="Button 1")
button1.pack(pady=10, padx=20, fill="x")

button2 = tk.Button(root, text="Button 2")
button2.pack(pady=10, padx=20, fill="x")

button3 = tk.Button(root, text="Button 3")
button3.pack(pady=10, padx=20, fill="x")

root.mainloop()