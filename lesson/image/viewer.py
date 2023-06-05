from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
def show_image(img):
    global window
    window = Tk()
    tk_image = ImageTk.PhotoImage(img)
    Label(window, image=tk_image).pack()
    def stop(event=None):
        window.destroy()
    window.bind('<Escape>', stop)
    window.bind('q', stop)
    window.mainloop()
def show_images(img1, img2):
    global window
    window = Tk()
    tk_image1 = ImageTk.PhotoImage(img1)
    tk_image2 = ImageTk.PhotoImage(img2)
    Label(window, image=tk_image1).pack(side=LEFT)
    Label(window, image=tk_image2).pack(side=LEFT)
    def stop(event=None):
        window.destroy()
    window.bind('<Escape>', stop)
    window.bind('q', stop)
    window.mainloop()

#cat_img = Image.open('zophie.png')
# img = Image.open('pink.png')
# show_images(cat_img, img)



