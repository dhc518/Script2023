import logging
from tkinter import *
from tkinter.ttk import *

# from customtkinter import *
# from customtkinter import CTk as
# Tk = CTk
# Frame = CTkFrame
# Label = CTkLabel
# Button = CTkButton
# Entry = CTkEntry
# ScrolledText = CTkTextbox
# Checkbutton = CTkCheckBox
# Radiobutton = CTkRadioButton


window = Tk()
window.title("My Tkinter App")
window.geometry("640x480+1200+50")
window.resizable(False,False)

#보이지 않는 액자
first_line_frame = Frame(window)
first_line_frame.pack()

label = Label(first_line_frame, text='hello, world') # 생성
label.pack(side="left")
#label.place(x=100, y=100)

def rotate():
    #logging.info('Pressed')
    text = label.cget('text')
    text = text[1:] + text[0]
    label.config(text=text)

button = Button(first_line_frame, text='PUSH', command=rotate)
button.pack(side="top")

def change_text(event=None):
    new_text = entry.get()
    label.config(text=new_text)


entry = Entry(first_line_frame, width=50)
entry.bind('<Return>', change_text)
entry.pack(side="top")

#대용량 텍스트
from tkinter.scrolledtext import ScrolledText

wiki_python = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.[33]
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[34][35]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[36] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[37]
Python consistently ranks as one of the most popular programming languages.[38][39][40][41]
'''
text = ScrolledText(window, width=50, height=20, font=("consolas", 10))
text.insert(END, wiki_python)# 텍스트 위젯 내부의 텍스트 맨 킅 부분
text.pack(fill=BOTH, expand=True, padx= 10,  pady =10)# 남은 부분을 꽉 채워라

#color tag
text.tag_config('YELLOW', background='yellow', foreground='red')
text.tag_add('YELLOW', '2.0', '2.10')

#check button
def over18_clicked():
    print(f'{over18.get()=}')
over18 = IntVar() # 버튼값 연계용 정수 변수
cb = Checkbutton(window, text='over 18', command=over18_clicked, variable=over18)
over18.set(0)
cb.pack()

#여러개 중 하나 선택할 수 있는 라디오버튼
def gender_updated(var, index, mode):
    print(f'{var=}{mode=}{index=}')
    print(f'{gender.get()=}')

gender = StringVar(value='male')
Radiobutton(window, text='Male', value='male', variable=gender).pack()
Radiobutton(window, text='Female', value='female', variable=gender).pack()
gender.trace_add('write', gender_updated)

def stop(event=None):
    window.quit()

window.bind('<q>', stop)
window.mainloop()