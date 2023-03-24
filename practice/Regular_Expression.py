# 텍스트의 패턴을 나타내는 규칙 정의
#다양한 조건의 패턴을 쉽게 검색, 필요에 따라 교체
import re

#문자열 검색
# hello_re = re.compile(r'hello')
# hello_re.search('hello world')
# print(hello_re.search('hello world, hellow world, hello you'))
# print(hello_re.search('test'))

#전화번호 검색
# phone_re = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
# mo = phone_re.search('My number is 010-5555-4242.')
# print('Phone number found: ' + mo.group())

#그룹화 괄호 사용
# phone_re = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')
# mo = phone_re.search('My number is 415-5555-4242')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(0))
# print(mo.group())
# print(mo.groups())
# area_code, main_number = mo.groups()
# print(area_code)
# print(main_number)

#pipe | - 여러개 그룹을 동시에 매칭
# idol_re = re.compile(r'로제|제니')
# idol_re = re.compile(r'로제|제니')
# mo = idol_re.search('로제와 제니')
# print(mo.group())
# mo = idol_re.search('로제와 제니')
# print(mo.group())
# idol_re = re.compile(r'블랙핑크 (지수|로제|제니)')

# ? - 없거나 하나 있는 요소에 대한 매칭
# bat_re = re.compile(r'Bat(wo)?man')
# mo1 = bat_re.search('The Adventures of Batman')
# print(mo1.group())
# mo2 = bat_re.search('The Adventures of Batwoman')
# print(mo2.group())
#
# phone_re = re.compile(r'(\d\d\d-)?(\d\d\d\d-\d\d\d\d)')
# mo = phone_re.search('My number is 010-8041-0114')
# print(mo.group())
# mo = phone_re.search('My number is 8041-0114')
# print(mo.group())

# * 없거나 여러번 반복되는 요소에 대한 매칭
# + 한번 또는 여러번 반복되는 요소에 대한 매칭
# bat_re = re.compile(r'Bat(wo)*man')
# mo1 = bat_re.search('The Adventures of Batman')
# print(mo1.group())
# mo2 = bat_re.search('The Adventures of Batwoman')
# print(mo2.group())
# mo3 = bat_re.search('The Adventures of Batwowowowoman')
# print(mo3.group())
#
# bat_re = re.compile(r'Bat(wo)+man')
# mo1 = bat_re.search('The Adventures of Batwoman')
# print(mo1.group())
# mo2 = bat_re.search('The Adventures of Batwowowowoman')
# print(mo2.group())

# {x,y} - 특정 횟수만큼 반복되는 요소에 대한 매칭
# ha_re = re.compile(r'(Ha){3}')
# mo1 = ha_re.search('HaHaHa')
# print(mo1.group())
# mo2 = ha_re.search('Ha')
# print(mo2 == None)
#
# p = re.compile(r'(Ha){3,5}') # 가장 긴 것으로 매치
# p = re.compile(r'(Ha){3,5}?') # 가장 먼저 나온 것을 매치

#findall
# phone_re = re.compile(r'(\d\d\d-)?(\d\d\d\d-\d\d\d\d)')
# phone_re.findall('My number is 010-8041-0114, 010-1234-5678')
# phone_re.findall('My number is 8041-0114, 1234-5678')

#Character Class
# \d 0부터 9까지
# \D 숫자가 아닌 모든 문자
# \w 글자 숫자 그리고_
# \W \w 가 아닌 모든 문자
# \s 공백, 탭, 개행문자(\n)-white space
# \S \s 가 아닌 모든 문자

#[] - 문자 클래스 사용자 지정
# (a|b|c|e|f|g)
# [abcdefg]
# [a-g]
# [aeiouAEIOU] 모음
# [^aeiouAEIOU] 자음
# [a-zA-Z0-9]

# ^ - 문자열의 사작을 매칭, $ - 문자열의 마지막을 매칭
# p = re.compile(r'^hello')
# print(p.search('hello world'))
# print(p.search('She say hello'))
#
# p = re.compile(r'hello$')
# print(p.search('hello world'))
# print(p.search('She say hello'))

# . - new line 을 제외한 모든 문자와 매칭
# p = re.compile('.at')
# print(p.findall('The cat in the hat sat on the flat mat'))
#
# p = re.compile(r'.{1,2}치')
# print(p.findall('참치 꽁치 쥐치 가물치'))

# .* - 모든 문자열에 매칭
# p = re.compile(r'성:(.*)이름:(.*)')
# mo = p.search('성: 두 이름: 혁찬')
# print(mo.group())
# mo = p.search('성: 이름: ')
# print(mo.group())
# print(mo.groups())
# mo = p.search('성:이름:')
# print(mo.group())
# print(mo.groups())
#
# p = re.compile(r'<.*>')# 처음부터 끝까지
# print(p.search('<두혁찬> 님 입장하셨습니다.>'))
# p = re.compile(r'<.*?>')#꺽새 안에만
# print(p.search('<두혁찬> 님 입장하셨습니다.>'))

# new line \n 매칭 = DOTALL
# text = '''This
# is
# multiple
# lines
# '''
# p = re.compile('.*')
# p.search(text)
# p = re.compile('.*', re.DOTALL)
# p.search(text)

# I - 대소문자 무시
# p = re.compile(r'hello', re.I)
# p.search('HELLO WORLD').group()
# p.search('Hello World').group()

# sub() - 문자열 교체
#p = re.compile(r'<\D{2,4}>')
p = re.compile(r'<(\D)(\D{1,3})>')# 한 글자 성 과 이름 그룹화
p.search('제1회 복권 당첨자는 <두혁찬>입니다.')
p.sub('***','제1회 복권 당첨자는 <두혁찬>입니다.')
p.sub(r'\1**','제1회 복권 당첨자는 <두혁찬>입니다.')# 첫번째 매칭된 것을 지칭

# VERBOSE - 복잡한 정규식의 쉬운 표시 방법