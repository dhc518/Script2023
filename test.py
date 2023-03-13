##############인터닝 최적화##############
# a = 'he llo'
# b = 'he llo'
# print(a is b)

############print()의 기능################
# print('Hello', end='')
# print('World')
# print('cats', 'dogs', 'mice', sep=', ')

############local & global 참조(scope에 대해서)################
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

# ##############List##############
# #Shift+Alt+E
# num = '0123456789ABCDEF'
# num[::-1]
# mun = '0123456789ABCDEF'[::-1]
#
# spam = [['cat', 'bat'], [10,20,30,40,50]]
# spam[1][3]
# black_pink = ['jisu', 'jeni', 'rose', 'risa']
#
# black_pink[-2]
# len(black_pink)
# black_pink[0] = 'daehyun'
# black_pink.append('jyp')
# black_pink += ['YB']
# black_pink.remove('jyp')
# black_pink
# del black_pink[0]
# black_pink.insert(2, 'IU')
# # 가장 쉬운 방법
# for member in black_pink:
#     print(member)
# # C 스러운 방법
# for i in range(len(black_pink)):
#     print(i,black_pink[i])
# #enumerate 사용
# for i, member in enumerate(black_pink):
#     print(i, member)
# #멤버가 있는 지 판별?
# 'YB' not in black_pink
# black_pink.index('YB')
#
# #######sort#######
# spam = [2,5,3,14,1,-7]
# spam.sort(reverse=True)
# spam
#
# #######도플갱어와 복제인간###########
# data = ['A','B','C','D']
# new_data = data #도플갱어
# new_data is data
# id(new_data) == id(data)
# new_data[0] = 'X'
# data
# new_data = data.copy() #복제
# new_data == data
#
# ##############List Comorehension################
# value = [i for i in range(10)]
# value
# odd_values = [n for n in range(20) if n % 2 == 1]
# odd_values
# [(x,y) for x in [1,2,3,] for y in ['a','b','c']]
# vec = [[1,2,3],[4,5,6],[7,8,9]]
# [num for elem in vec for num in elem]
# import random
# values = [random.randint(0,5) for i in range(20)]
# values
# [v if v != 0 else 'zero' for v in values]
#
# ###########Tuple############
# t1 = (3,2,3)
# type(t1)
# t1[0]=2 #튜플은 값 변경 불가능, 변경 만 가능
# t2 = (100,)
# type(t2)
# t3 = (100)
# type(t3)
# t4 = ()
# type(t4)
# t5 = (2,3,4,5)
# t6 = (5,6,7,8)
# t5 + t6

##############가변 개수 사용 방법#################
# def add(*values): #앞에 *붙이면 인자를 튜플로 인식
#     result = 0
#     for v in values:
#         result += v
#     return result #sum(values)
#
# add(1,2,3,add(16546,134,3654651))
###################과제03########################
# def merge(*values):
#     sentence = ''
#     for word in values:
#         if values[0] == values[-1]:
#             sentence = word
#         elif word == values[-1]:
#             sentence= sentence + 'and ' + word
#         else:
#             sentence = sentence + word + ', '
#
#     return sentence
#
# final = merge('orange', 'apple', 'mango', 'banana', 'peanut')
# print(final)
#
# final = merge('orange')
# print(final)























