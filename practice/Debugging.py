# 버그의 이유
#     예상치 못한 입력, 예상치 못한 사용자
#     알고리즘의 오류(논라적안 오류)
#     부족한 시간 투자 -> 스트레스

# 디버깅 방법
#     중수 - 실시간 디버깅
#     고수 - 테스트 자동화

# 예외 발생(Rasing Exception)
#     예외처리
#     if
#     try - except
#     Raising Exceotions

# Exceotion Handling
# try:
#     age = int(input('Enger Age : '))
#     if age < 18:
#         #raise Exception
#         raise  ValueError('Too Young')
# except Exception as err:
#     print(f'{err=}, {type(err)=}')

# Exception raise
# def print_box(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a singke chracter string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')
#
#     print(symbol * width)
#     for i in range(height-2):
#         print(symbol + (' ' * (width-2)) + symbol)
#     print(symbol * width)
#
# for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('zz', 3, 3)):
#     try:
#         print_box(sym, w, h)
#     except Exception as err:
#         print('An exception happened: ' + str(err))

#Traceback
# import traceback
# def bacon():
#     try:
#         raise Exception('My Error')
#     except:
#         with open('error_story.txt', 'a') as ef:
#             for line in traceback.format_stack():
#                 ef.write(line)
# def spam():
#     bacon()
# def ham():
#     spam()
# ham()

# 표명(Assertion)
# 1번 예시
# data = 100
# assert data == 100
# assert data < 100
# 2번 예시
# age = input('Enter Age: ')
# assert type(age) is int, "age should be integer"

# Exception vs. Assertion
# ▪ Exception
#   ▪ 주로 사용자 입력에 따른 오류
#   ▪ 예상하지 못한 상황에 대한 처리를 못한 “버그”
#   ▪ 추후 버그 수정을 위해서, 코드 내에 exception 처리는 유지되고 실행됨.

# ▪ Assertion
#   ▪ 심각한, 중대한 버그.
#   ▪ 개발 단계에서, 반드시 해결해야 함.
#   ▪ 실행 속도를 저하시키기 때문에, release build 에서는 빠져야 함. -O 최적화 옵션.
#   ▪ python -O mycode.py

# Logging
# print 대신 logging
import logging

# basic config works only once after logging
logging.basicConfig(
    filename='mylog.txt',
    level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s - %(message)s'
)

a = 10
logging.debug('this is debug')
logging.warning(f'value {a= } is a warning')
logging.info('this is simple info')
logging.error('error')
logging.critical('critical error')


# Pycharm Debugging
