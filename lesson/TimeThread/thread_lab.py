import threading
from queue import Queue

def calc(queue, number=100**4, show='*'):
    sum =0

    for i in range(number):
        if i % (number//10) ==  0:
            print(f'{show*5}{int(i//(number/10))}', end='')
        sum += i

    queue.put(f'\n 1 to {number} {sum = }')




result = Queue()

thread1 = threading.Thread(target=calc, args=[result]).start()
thread2 = threading.Thread(target=calc, args=[result, 10**3,'+']).start()
thread3 = threading.Thread(target=calc, args=[result, 10**8,'$']).start()
print(result.empty())
while result.empty():
    pass
# print(f'\n{result.empty()}')
# thread1.join()
# print(f'\n{result.empty()}')

print(result.get())
print('all thread end')