'''
tkinter documentation: https://docs.python.org/3/library/tkinter.html#handy-reference

upload file:
https://www.plus2net.com/python/tkinter-filedialog-upload-display.php

https://www.youtube.com/watch?v=bdKxTH7Y-38&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=101
'''

import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

### fixed variable
WIDTH = 640
HEIGHT = 400

### Function to upload
def upload_clicked():
    filename = filedialog.askopenfilename(initialdir="C:/Users/Hiroyuki Ishige/Pictures", title="Selected File",
                                      filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))


    img1 = ImageTk.PhotoImage(Image.open(filename))

    # label_img = Label(image=img1)
    # label_img.grid(column=0, row=3)
    canvas_1.create_image(WIDTH/2, HEIGHT/2, image=img1)

### Main window
window = Tk()
window.title("Watermakr application")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=20, pady=20)  # padding for window

### Title
label_title = Label(text="Please upload photo", font=("Arial", 15))
label_title.grid(column=0, row=0)
# my_label.config(text="Label") #When you would like to change label title

### Buttun to upload
button_upload = Button(text="Upload", command=upload_clicked)
button_upload.grid(column=1, row=0)

# Watermark input window
label_watermark = Label(text="Please input words for watermark", font=("Arial", 15))
label_watermark.grid(column=0, row=1)
label_watermark.config(padx=20, pady=20)

input_watermark = Entry(width=20)
input_watermark.grid(column=1, row=1)

# Create Canvas_1
canvas_1 = Canvas(window, width=WIDTH/2, height=HEIGHT/2, bg="white")
canvas_1.grid(column=0, row=2)

window.mainloop()
