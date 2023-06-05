import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def collage_image():
    global image_list
    global collage
    collage_width = len(image_list) * 100  # 콜라주된 이미지 너비
    collage = Image.new('RGB', (collage_width, 100))  # 콜라주된 이미지 크기
    x = 0
    for img in image_list:
        img = img.resize((100, 100))  # 이미지 크기 조정
        collage.paste(img, (x, 0))
        x += 100
    display_image(collage)

def display_image(img):
    img = img.resize((img.size[0] // 2, img.size[1] // 2))  # 출력할 이미지 크기 조정
    tk_image = ImageTk.PhotoImage(img)
    image_label.configure(image=tk_image)
    image_label.image = tk_image

def save_image():
    global collage
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
    if file_path:
        collage.save(file_path)  # 콜라주된 이미지 저장
        print("이미지 저장 완료")

def open_image():
    global image_list
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png *.jpg")])
    for file_path in file_paths:
        img = Image.open(file_path)
        image_list.append(img)
    display_image_collage()

def display_image_collage():
    collage_width = len(image_list) * 100
    collage_height = 100
    collage = Image.new('RGB', (collage_width, collage_height))
    x = 0
    for img in image_list:
        img = img.resize((100, 100))
        collage.paste(img, (x, 0))
        x += 100
    display_image(collage)

root = tk.Tk()

image_list = []

# 버튼 및 레이블 생성
open_button = tk.Button(root, text="이미지 열기", command=open_image)
open_button.pack()

convert_button = tk.Button(root, text="변환", command=collage_image)
convert_button.pack()

save_button = tk.Button(root, text="저장", command=save_image)
save_button.pack()

image_label = tk.Label(root)
image_label.pack()

root.mainloop()
