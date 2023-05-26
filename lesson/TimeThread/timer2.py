import threading
import datetime


prev_callback_timer = datetime.datetime.now()
def callback():
    global prev_callback_timer
    now = datetime.datetime.now()
    delta = now - prev_callback_timer
    prev_callback_timer = now
    print(f'callback @{now} ({delta})')

looping = True

def simple_timer():
    global prev_callback_timer

    while looping:
        now = datetime.datetime.now()
        if now >= prev_callback_timer + datetime.timedelta(seconds=1):
            callback()
            prev_callback_timer = now

thread = threading.Thread(target=simple_timer)
thread.start()