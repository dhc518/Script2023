# 시간 측정
import time

# def calc():
#     global prod
#     prod = 0
#     for i in range(1, 100000000):
#         prod += i

# start_time = time.time()
# calc()
# end_time = time.time()
#
# print(f'{prod=} in {end_time-start_time} sec')
#
# import timeit
# timeit.timeit(calc, number=1)

# import cProfile
# print(cProfile.run('calc()'))

# time.gmtime() # 현재 시각, UTC 기준
# time.gmtime(0) # EPOC time
# time.gmtime(1000000000)
# time.localtime() # 현재 지역 시각
# time.localtime(0) # 현재 지역에서 0초가 경과했을 때,
# time.ctime()
# time.ctime(0)
# time.timezone # 9 hours * 60 min * 60 secs
# time.tzname

# import datetime
#
# now = datetime.datetime.now()
# a = now.strftime('%Y/%m/%d %H:%M:%S')
# b = now.strftime('%I:%M %p')
# c = now.strftime("%B of %y")
#
# print(a)
# print(b)
# print(c)
#
# a = datetime.datetime.strptime('August 22, 1970', '%B %d, %Y')
# b = datetime.datetime.strptime('2021/08/22 13:29:00', '%Y/%m/%d %H:%M:%S')
# c = datetime.datetime.strptime("August of '70", "%B of '%y")
#
# print(a)
# print(b)
# print(c)


import calendar
# calendar.setfirstweekday(6)
# print(calendar.month(2023, 5))
cal = calendar.Calendar(firstweekday=6)
for date in cal.itermonthdates(2023, 6):
    print(date)

for day in cal.itermonthdays(2023, 6):
    print(day)
for day in cal.itermonthdays2(2023, 6):
    print(day)
for day in cal.itermonthdays3(2023, 6):
    print(day)
for day in cal.itermonthdays4(2023, 6):
    print(day)



cal = calendar.Calendar(firstweekday=6)

