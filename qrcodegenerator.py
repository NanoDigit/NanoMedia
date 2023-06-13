import tkinter as tk
from tkinter import messagebox
from qrcodeutil import qrcodeutil

def generateCode():
    size = size_entry.get()
    text = text_entry.get()
    loc = loc_entry.get()
    name = name_entry.get()

    # Validate input
    if not (size and text and loc and name):
        messagebox.showerror("Error", "Please fill all the questions.")
        return

    try:
        size = int(size)
    except ValueError:
        messagebox.showerror("Error", "Size must be a number.")
        return

    qrcoder = qrcodeutil()
    success = qrcoder.generateCode(size, text, loc, name)
    if success:
        messagebox.showinfo("QR Code Generator", "QR Code saved successfully!")
    else:
        messagebox.showerror("Error", "Failed to save QR Code.")

window = tk.Tk()
window.title("QR Code Generator")
window.geometry("400x300")

input_frame = tk.Frame(window, pady=10)
input_frame.pack()

size_label = tk.Label(input_frame, text="QR Code Size:")
size_label.grid(row=0, column=0, sticky="e")
size_entry = tk.Entry(input_frame, width=20)
size_entry.grid(row=0, column=1)

text_label = tk.Label(input_frame, text="Text:")
text_label.grid(row=1, column=0, sticky="e")
text_entry = tk.Entry(input_frame, width=20)
text_entry.grid(row=1, column=1)

loc_label = tk.Label(input_frame, text="File Location:")
loc_label.grid(row=2, column=0, sticky="e")
loc_entry = tk.Entry(input_frame, width=20)
loc_entry.grid(row=2, column=1)

name_label = tk.Label(input_frame, text="File Name:")
name_label.grid(row=3, column=0, sticky="e")
name_entry = tk.Entry(input_frame, width=20)
name_entry.grid(row=3, column=1)

button_frame = tk.Frame(window)
button_frame.pack()

generate_button = tk.Button(button_frame, text="Generate QR Code", command=generateCode)
generate_button.pack(pady=10)

window.mainloop()