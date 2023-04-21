# CSV(Comma Separated Value)
# ▪ 여러 개 항목값들의 집합을 텍스트 형식으로 저장
# ▪ 쉼표로 구분함. (기본 delimiter 는 쉼표)
# ▪ 스프레드쉬트 데이타의 기본 구조

import csv

# f = open('simple.csv', newline='')
# reader = csv.reader(f, quotechar="'",
#                     delimiter=":",
#                     skipinitialspace=True)
# for line in reader: # reader iterator
#     print(line)
# f.close()

# 항목과 값들을 연관시키기 - DictReader
# f = open('oscar_age_female.csv')
# reader = csv.DictReader(f, skipinitialspace=True)
# for line in reader:
#     print(line)
# f.close()

# writer
# f = open('test.csv', 'w', newline='')
# writer = csv.writer(f, delimiter='|',
#                     quoting=csv.QUOTE_ALL,
#                     quotechar='*')
# writer.writerow([100, 176, 90])
# writer.writerow([101, 180, 76])
# writer.writerow(['hello, world', 20, 10])
# writer.writerows(
#     [
#         [1,2,3],
#         [4,5,6]
#     ]
#
# )
# f.close()

#dict writer
with open('test.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['kor', 'math', 'eng'])
    writer.writeheader()
    writer.writerow({'kor':100, 'math':95, 'eng':90})
    writer.writerow({'kor':55, 'math':70, 'eng':20})

