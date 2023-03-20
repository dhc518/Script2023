import keyboard
import pyperclip

word = pyperclip.paste()
splitted_word = word.split()

count = {}
for w in splitted_word:
    if w.isalpha():
        count.setdefault(w, 0)
        count[w] = count[w] + 1

print(count)