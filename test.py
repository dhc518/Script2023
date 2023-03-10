##############인터닝 최적화##############
# a = 'he llo'
# b = 'he llo'
# print(a is b)

############print()의 기능################
# print('Hello', end='')
# print('World')
# print('cats', 'dogs', 'mice', sep=', ')

############local & global 참조################
# def spam():
#     #global eggs
#     print(eggs)
#     #eggs = 'spam local'
#eggs = 'global'
# spam()

#############함수 데이터 타입의 유연성###############
# def sum(a, b):
#     return  a + b
#print(sum('Hundred', '100'))

#############예외 처리###############
# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Zero Divide')
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

#############sum()###############
# numbers = [1,2,3,4,10]
# print(sum(numbers))
# sum = 0
# for i in numbers:
#     sum += i
# print(sum)

##############any(), all()##############
# import random
# ages = [random.randint(1,100) for n in range(20)]
# if any(i < 18 for i in ages):
#     print('미성년자 있음.')
# else:
#     print('모두 다 성인임')
#
# print('모두 다 성인임') if all(i >= 18 for i in ages) else print('미성년자 있음.')

#############filter() 집합들의 데이터들을 부류, 걸러냄###############
#numbers = [random.randint(0,99) for i in range(20)]
# def mul3_filter(n):
#     return n % 3 == 0
# result = list(filter(mul3_filter, numbers))
# print(result)
# result = list(filter(lambda  n: n % 3 == 0, numbers))
# print(result)

###############map() 집합들의 데이터들을 한꺼번에 변환#############
# def square(x):
#     return x ** 2
# numbers = [1,2,3,4,5]
# squares = map(square, numbers)
# squares_list = list(squares)
# print(squares_list)
# squares_list = list(map(lambda n: n ** 2, numbers))
# print(squares_list)

##############min(), max(), sum()##############
# min(1,2,3,4)
# max([100,2,2,3])
# sum([n for n in range(1,100+1)])

###############zip()#############
# names = ["Alice", "Bob", "Charlie"]
# ages = [25,30,35]
# heights = [180.,172.1, 185.3]
# zipped = zip(names, ages, heights) #배열 요소들을 차례로 집합
# print(list(zipped))
# print(list(zipped)) #한번 사용하면 소진됨.
