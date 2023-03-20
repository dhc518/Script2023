########다양한 문자열 처리 함수########
#Double quote / Escape character
# spam = "That is Alice's cat"
# spam = 'say hi to Bob\'s mother'

#Raw String
# print(r'That is Carol\'s cat.')# esc 키 무시

#Multiple Lines
# print('''
# 애국가
#     동해물과 백두산이 ....
#     우리나라 만세....
# 끝.
# ''')
"""
멀티플 코멘트 라인
"""

#Slicing
# message = 'hello, world'
# even_message = message[::2]

#문자열 포함여부
# 'Hello' in 'Hello World'
# 'Hello' in 'Hello'
# 'HELLO' in 'Hello World'
# '' in 'spam'
# 'Hello' not in 'Hello World'
#
# #isX
# 'hello'.isalpha()
# 'hello'.isalnum()
# '\n\t\r\v  '.isspace()
# 'This is Title Case'.istitle()
# 'This is not Title Case'.istitle()
#
# #upper,lower,isupper,islower
# spam = 'Hello world!'
# spam = spam.upper()
# spam = spam.lower()
# spam.isupper()
# spam.islower()
#
#
#
# #startswith, endswith
# 'Hello world!'.startswith('Hello')
# 'Hello world!'.endswith('world!')
#
# #join
# ', '.join(['cats', 'rats', 'bats'])
#
# #split 화이트 스페이스를 기준으로 띄워줌
# 'My name is Doo'.split()
# 'My name is Doo\nI love you'.split()
# 'My name is Doo'.split(' ')
# 'My name is        Doo'.split(' ')
# 'My name is Doo'.split('m')
# 'My namme is Doo'.split('m')
# 'My name is Doo'.split('is')
# #줄단위 분리도 가능
#
# #partition 결과가 튜플로 나옴, 구분자도 같이 알려줌
# 'My name is Doo'.partition('m')
#
# #center,rjust,ljust
# 'hello'.rjust(10)
# 'hello'.ljust(10)
# 'hello'.rjust(10, '*')
# 'hello'.center(10,'$')
#
# #strip,rstrip,lstrip
# d = '    hello   world      '
# d.strip()
# d.lstrip()
# d.rstrip()
#
# #ord(),chr()
# ord('A')
# chr(65)
#
# ########클립보드 처리########
# import pyperclip
#
# pyperclip.copy('Hello from Python')
#
# pyperclip.paste()

########핫키 처리########
import keyboard

def write_alphabet():
    keyboard.write('abcdefghijklmnopqrstuvwxyz')

keyboard.add_hotkey('shift+windows+w', write_alphabet)
keyboard.wait('esc')
keyboard.remove_all_hotkeys()
