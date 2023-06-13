import tkinter as tk
from tkinter import messagebox
from qrcodeutil import qrcodeutil
#pip install pillow to get this package
from PIL import ImageTk,Image

def saveCode():
    if qrcoder.Image == None:
        return
    if qrcoder.saveQR()== True:
        messagebox.showinfo("QR Code Generator", "QR Code is saved successfully as " + qrcoder.fullFile +"!")
    else:
        messagebox.showinfo("QR Code Generator", "QR Code FAILURE " + qrcoder.fullFile +"!")
    return

# Generate QR Code function
def generateCode():
    if text_entry.get()=="":
        return
    qrcoder.setSize(size_entry.get(),text_entry.get(),loc_entry.get(),name_entry.get())
    ret = qrcoder.generateQR()
    if ret == True:
        rawImage = qrcoder.Image.resize((200,200))
        img = ImageTk.PhotoImage(rawImage)  
        
        pic_label = tk.Label(window,image=img)
        pic_label.pack()        
        window.mainloop()

window = tk.Tk()
window.title("QR Code Generator")
window.geometry("200x400")

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

save_button = tk.Button(window, text="Save QR Code", command=saveCode)
save_button.pack(pady=10)
qrcoder = qrcodeutil()

window.mainloop()