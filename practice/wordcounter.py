import keyboard
import pyperclip

def keyboard_print():
    str_count = word_processing()
    print(str_count)
    # for word, count in count.items():
    keyboard.write(str_count)

def word_processing():
    word = pyperclip.paste()
    splitted_word = word.split()
    count = {}
    for w in splitted_word:
        if w.isalpha():
            count.setdefault(w, 0)
            count[w] = count[w] + 1
    str_count = str(count)
    #print(str_count)
    special_chars = "!@#$%^&*()-_=+`~[]\\{}|;:'\".<>/?"
    for char in special_chars:
        str_count = str_count.replace(char, "")
        str_count = str_count.replace(",", "\r")
    return str_count



keyboard.add_hotkey('shift+windows+w', keyboard_print)
keyboard.wait('esc')
keyboard.remove_all_hotkeys()


