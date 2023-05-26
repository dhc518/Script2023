import threading
import datetime


prev_now = datetime.datetime.now()
def callback():
    global prev_now
    now = datetime.datetime.now()
    delta = now - prev_now
    prev_now = now
    print(f'callback @{now} ({delta})')

looping = True

def simple_timer():
    global prev_now
    while looping:
        now = datetime.datetime.now()
        if now.second != prev_now.second:
            callback()
            prev_now = now

thread = threading.Thread(target=simple_timer)
thread.start()