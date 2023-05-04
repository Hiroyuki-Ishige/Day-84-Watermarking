'''
tkinter documentation: https://docs.python.org/3/library/tkinter.html#handy-reference

upload file:
https://www.plus2net.com/python/tkinter-filedialog-upload-display.php

https://www.youtube.com/watch?v=bdKxTH7Y-38&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=101

https://mulberrytassel.com/python-practice-dialog-1/ ###Upload file

https://mulberrytassel.com/python-practice-pil-2/ ###Upload file

https://office54.net/python/tkinter/textbox-get-insert ### get words in text box

https://tat-pytone.hatenablog.com/entry/2021/09/26/131945 ### add watermark

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
    global img1_tk  # need to set as global variable because main window is outside of this function

    ### import image file
    filename = filedialog.askopenfilename(initialdir="C:/Users/Hiroyuki Ishige/Pictures", title="Selected File",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    ### set size of image
    img1 = Image.open(filename)
    pic_width = int(img1.width / 6)
    pic_height = int(img1.height / 6)

    ### resize image
    img1_tk = ImageTk.PhotoImage(image=img1.resize((pic_width, pic_height)))

    ### Create Canvas_1
    canvas_1 = Canvas(window, width=pic_width, height=pic_height, bg="white")
    canvas_1.grid(column=0, row=2)

    ### show image on cavas
    canvas_1.create_image(0, 0, anchor="nw", image=img1_tk)

    ### print watermark text
    print(input_watermark.get())


### Set main window
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

### Input watermark word
label_watermark = Label(text="Please input words for watermark", font=("Arial", 15))
label_watermark.grid(column=0, row=1)
label_watermark.config(padx=20, pady=20)

input_watermark = Entry(width=20)
input_watermark.grid(column=1, row=1)
input_watermark.insert(tkinter.END, "Please fill in")


### event roop
window.mainloop()
