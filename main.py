'''
tkinter documentation: https://docs.python.org/3/library/tkinter.html#handy-reference

upload file:
https://www.plus2net.com/python/tkinter-filedialog-upload-display.php

https://www.youtube.com/watch?v=bdKxTH7Y-38&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=101
'''

from tkinter import *

window = Tk()
window.title("Watermakr application")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # padding for window

# Title
label_title = Label(text="Please upload photo", font=("Arial", 15))
# label_title.pack()
label_title.grid(column=0, row=0)


# my_label.config(text="Label") #If you would like to change

# Button
def upload_clicked():
    label_title.config(text="File Uploaded")


button_upload = Button(text="Upload", command=upload_clicked)
# button_upload.pack()
button_upload.grid(column=1, row=0)

# Watermark
label_watermark = Label(text="Please input words for watermark", font=("Arial", 15))
# label_watermark.pack()
label_watermark.grid(column=0, row=2)
label_watermark.config(padx=20, pady=20)

input_watermark = Entry(width=20)
# input_watermark.pack()
input_watermark.grid(column=1, row=2)

window.mainloop()
