import tkinter as tk
from tkinter import messagebox,Canvas
from qrcodeutil import qrcodeutil
#pip install pillow to get this package
from PIL import ImageTk,Image


# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create labels and entry fields
size_label = tk.Label(window, text="QR Code Version:")
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

qrcoder = qrcodeutil()


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
    if text.get()=="":
        return
    qrcoder.setSize(size.get(),text.get(),loc.get(),name.get())
    ret = qrcoder.generateQR()
    if ret == True:
        rawImage = qrcoder.Image.resize((200,200))
        img = ImageTk.PhotoImage(rawImage)  
        
        pic_label = tk.Label(window,image=img)
        pic_label.pack()        
        window.mainloop()

# Generate button
generate_button = tk.Button(window, text="Generate QR Code", command=generateCode)
generate_button.pack()

save_button = tk.Button(window, text="Save QR Code", command=saveCode)
save_button.pack()
print("FOOOF")
# Start the Tkinter event loop
window.mainloop()