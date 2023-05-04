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
from PIL import Image, ImageTk, ImageDraw, ImageFont

### fixed variable
WIDTH = 640
HEIGHT = 400


# Function to upload
def upload_clicked():
    global img1_tk  # need to set as global variable because main window is outside of this function

    # import image file
    filename = filedialog.askopenfilename(initialdir="C:/Users/Hiroyuki Ishige/Pictures", title="Selected File",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    # set size of image and convert to RGBA
    img1 = Image.open(filename).convert("RGBA")
    pic_width = int(img1.width / 6)
    pic_height = int(img1.height / 6)

    # set empty image to write watermark word. Same size of img1.
    txt = Image.new("RGBA", img1.size, (255, 255, 255, 0))

    # set font
    fnt1 = ImageFont.truetype("meiryo", int(img1.size[0] / 10))

    # Set image context
    d = ImageDraw.Draw(txt)

    # draw watermark with transparency
    color = (255, 255, 255, 128)  # 50% transparency
    d.text((int(img1.size[0] * 0.1), (int(img1.size[1] * 0.2))), input_watermark.get(),
           font=fnt1,
           fill=color)

    # alpha brend of image and watermark
    out = Image.alpha_composite(img1, txt)

    # resize image
    img1_tk = ImageTk.PhotoImage(image=out.resize((pic_width, pic_height)))

    # Create Canvas_1
    canvas_1 = Canvas(window, width=pic_width, height=pic_height, bg="white")
    canvas_1.grid(column=0, row=2)

    # show image on cavas
    canvas_1.create_image(0, 0, anchor="nw", image=img1_tk)

    # print watermark text
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
