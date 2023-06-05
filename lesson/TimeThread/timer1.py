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
    callback()
    if looping:
        threading.Timer(1, simple_timer).start()

simple_timer()