import tkinter as tk
from tkinter import messagebox
import qrcode
from qrcodeutil import qrcodeutil

# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create labels and entry fields
size_label = tk.Label(window, text="QR Code Size:")
size_label.pack()
size = tk.Entry(window)
size.pack()

text_label = tk.Label(window, text="Text to Encode:")
text_label.pack()
text = tk.Entry(window)
text.pack()

loc_label = tk.Label(window, text="File Location:")
loc_label.pack()
loc = tk.Entry(window)
loc.pack()

name_label = tk.Label(window, text="File Name:")
name_label.pack()
name = tk.Entry(window)
name.pack()

# Generate QR Code function
def generateCode():
    qrcoder = qrcodeutil()
    ret = qrcoder.generateCode(size.get(),text.get(),loc.get(),name.get())
    if ret == True:
        messagebox.showinfo("QR Code Generator", "QR Code is saved successfully!")
        return
    messagebox.showinfo("QR Code Generator", "Major failure")
    return
    qr = qrcode.QRCode(
        version=size.get(),
        box_size=10,
        border=5
    )
    qr.add_data(text.get())
    qr.make(fit=True)
    img = qr.make_image()
    fileDirec = loc.get() + '\\' + name.get()
    img.save(f'{fileDirec}.png')
    messagebox.showinfo("QR Code Generator", "QR Code is saved successfully!")

# Generate button
generate_button = tk.Button(window, text="Generate QR Code", command=generateCode)
generate_button.pack()

# Start the Tkinter event loop
window.mainloop()