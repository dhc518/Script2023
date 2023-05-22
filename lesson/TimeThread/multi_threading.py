import threading

logging = True

def calc(number=100000, show='*'):
    global looping
    looping = True
    prod = 1
    for i in range(1, number):
        if i % (number//10) ==  0:
            print(f'{show*3}{i//(number//10)}', end='')
        prod *= i
    print('\nCalculation Finished.')
    looping = False

calc()
print('Program ends, but looping is', looping)
thread = threading.Thread(target=calc)
thread.start()
print('Program ends, but looping is', looping)
