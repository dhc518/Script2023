import random

kor = [random.randint(1, 100) for _ in range(20)]
eng = [random.randint(1, 100) for _ in range(20)]
math = [random.randint(1, 100) for _ in range(20)]

print('''===============================================
Student     KOR     ENG     MATH        AVG
-----------------------------------------------
      ''')
i=0
while i <= 19:
    print(f'{i+1}           {kor[i]}       {eng[i]}       {math[i]}       {(kor[i]+eng[i]+math[1])/3}')
    i += 1
print('-----------------------------------------------')
print(f'AVG         {sum(kor)/20}     {sum(eng)/20}     {sum(math)/20}')
print('===============================================')

