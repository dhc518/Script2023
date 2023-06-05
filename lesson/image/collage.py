import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

count = 0

def collage_image():
    global image_list
    global collage
    collage = Image.new('RGB', (200, 200))  # 콜라주된 이미지 크기
    x = 0
    y = 0
    for img in image_list:
        img = img.resize((100, 100))  # 이미지 크기 조정
        collage.paste(img, (x, y))
        x += 100
        if x >= 200:
            x = 0
            y += 100
    #display_image(collage)
    tk_image = ImageTk.PhotoImage(collage)
    collage_label.configure(image=tk_image)
    collage_label.image = tk_image

def display_image(count, img):
    img = img.resize((200, 200))  # 출력할 이미지 크기 조정
    tk_image = ImageTk.PhotoImage(img)
    if count == 0:
        image_label1.configure(image=tk_image)
        image_label1.image = tk_image
    elif count ==1:
        image_label2.configure(image=tk_image)
        image_label2.image = tk_image
    elif count ==2:
        image_label3.configure(image=tk_image)
        image_label3.image = tk_image
    elif count ==3:
        image_label3.configure(image=tk_image)
        image_label3.image = tk_image


def save_image():
    global collage
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
    if file_path:
        collage.save(file_path)  # 콜라주된 이미지 저장
        print("이미지 저장 완료")

def open_image(count):
    global image_list
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg")])
    if file_path:
        img = Image.open(file_path)
        image_list.append(img)

        count = count % 4
        display_image(count, img)
        count += 1




root = tk.Tk()

image_list = []

# 버튼 및 레이블 생성
open_button = tk.Button(root, text="이미지 열기", command=open_image)
open_button.pack()

convert_button = tk.Button(root, text="변환", command=collage_image)
convert_button.pack()

save_button = tk.Button(root, text="저장", command=save_image)
save_button.pack()

image_label1 = tk.Label(root)
image_label1.pack(side=LEFT)
image_label2 = tk.Label(root)
image_label2.pack(side=LEFT)
image_label3 = tk.Label(root)
image_label3.pack(side=LEFT)
image_label4 = tk.Label(root)
image_label4.pack(side=LEFT)
collage_label = tk.Label(root)
collage_label.pack(side=BOTTOM)

root.mainloop()
