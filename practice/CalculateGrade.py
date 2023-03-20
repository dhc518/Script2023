import random
#
# kor = [random.randint(1, 100) for _ in range(20)]
# eng = [random.randint(1, 100) for _ in range(20)]
# math = [random.randint(1, 100) for _ in range(20)]
#
# print('''===============================================
# Student     KOR     ENG     MATH        AVG
# -----------------------------------------------
#       ''')
# i=0
# while i <= 19:
#     print(f'{i+1}           {kor[i]}       {eng[i]}       {math[i]}       {(kor[i]+eng[i]+math[1])/3}')
#     i += 1
# print('-----------------------------------------------')
# print(f'AVG         {sum(kor)/20}     {sum(eng)/20}     {sum(math)/20}')
# print('===============================================')

########해설########
def generate_score():
    #score = { 'kor':[random.randint(0,100) for n in range(20)], 'eng':[], 'math':[]} #dictionary
    score = [[random.randint(0,100)for j in range(3)]for n in range(20)]
    return score

def process_score(score):
    student_avg = [sum(score[n]) / 3 for n in range(20)]
    subject_avg = [sum([score[n][j]for n in range(20)]) / 20 for j in range(3)]
    return  subject_avg, student_avg

def print_score(score, student_avg, subject_avg):
    for n, s in enumerate(score):
        print(f'{n+1} {score[0]} {score[1]} {score[2]} {student_avg[n]}')

    pass


score = generate_score()
subject_avg, student_avg = process_score(score)
print_score(score, student_avg, subject_avg)


