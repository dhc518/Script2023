import pyautogui

im = pyautogui.screenshot('screen.png', region=(1176,749,500,285))
pyautogui.moveTo(1389,293)
pyautogui.drag(1576-1389,539-293, duration= 1)
pyautogui.click(1725,481)