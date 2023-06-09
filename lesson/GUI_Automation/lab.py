import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

w, h = pyautogui.size()

# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# for i in range(10):
#     pyautogui.move(100, 0, duration=1)
#     pyautogui.move(0, 100, duration=1)
#     pyautogui.move(-100, 0, duration=1)
#     pyautogui.move(0, -100, duration=1)

# pyautogui.click(63, 462)
#
# im = pyautogui.screenshot('screen.png', region=(0,0,100,100))
# im.show()

# rect = pyautogui.locateOnScreen('1.png')
# p = pyautogui.locateCenterOnScreen('1.png')
# pyautogui.click(p)
# pyautogui.click('2.png')
# all_rects = pyautogui.locateAllOnScreen('2.png')
# for rect in all_rects:
#               pyautogui.click(rect.left+rect.width//2,
#               rect.top+rect.height//2)
#     pyautogui.click(rect)

# pyautogui.click(469,300)
# pyautogui.scroll(-5000)
# pyautogui.scroll(5000)
#
# pyautogui.click(1171,539)
# pyautogui.typewrite('hello from professor\n', 0.25)

# import  pyperclip
# pyautogui.click(1171,539)
# pyperclip.copy('한글은 클리보더로, 두혁찬')
# pyautogui.hotkey('ctrl','v')
# pyautogui.typewrite('\n')

pyautogui.doubleClick(1411,724,duration = 1)
pyautogui.click(1466,807,duration = 1)
pyautogui.moveTo(1186,830,duration = 1)
pyautogui.drag(100,100,duration = 1)
pyautogui.click(1286,930,duration = 1)

