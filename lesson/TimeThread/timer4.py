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

    prev_delta = datetime.timedelta(0)
    while looping:
            now = datetime.datetime.now()
            delta = now - prev_now + prev_delta
            if delta >= datetime.timedelta(seconds=1):
                callback()
                prev_delta = delta - datetime.timedelta(seconds=1)
                prev_now = now

thread = threading.Thread(target=simple_timer)
thread.start()