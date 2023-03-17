text = 'It was a bright cold day in April, and the clocks were striking thirteen'

##ver.01##
# count = {}# 빈 딕셔너리를 만드는 방법
#
# for c in text:
#     count.setdefault(c, 0) #기존에 값이 있으면 무시.
#     count[c] += 1

##ver.02##
from collections import defaultdict

count = defaultdict(lambda: 0)
for c in text:
    count[c] += 1

print(count)
print(type(count))

