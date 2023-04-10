import re
import exrex

p = re.compile(r'''
    010|02|051|053|031|032|062|042|052
''', re.VERBOSE)

p = re.compile(r'''
    \(
    010|02|051|053|031|032|062|042|052
    \)
''', re.VERBOSE)

p = re.compile(r'''
    (010|02|051|053|031|032|062|042|052)
    |
    \(
    010|02|051|053|031|032|062|042|052
    \)
''', re.VERBOSE)



p = re.compile(r'''
    [ ]*-?[ ]*
''', re.VERBOSE)

#국번
p = re.compile(r'''
    [123456789]\d{2,3}
''', re.VERBOSE)

#개별 번호
p = re.compile(r'''
   \d{4}
''', re.VERBOSE)

p = re.compile(r'''
    ^
    (
        (
            (010|02|051|053|031|032|062|042|052)
            |
            \(
                (010|02|051|053|031|032|062|042|052)
            \)
        )
        [ ]*-?[ ]*
    )?
    [123456789]\d{2,3}
    [ ]*-?[ ]*
    \d{4}
    $
''', re.VERBOSE)


#테스트 코드

p.search('010')
p.search('02')
p.search('111')

good_numbers = [
    '3533435', '34239872', '353 3435', '01034243424',
    '(031)-8041-0123', '(010)-333 - 4444'
]

bad_numbers = [
    '010333344444', '010-3333-444', '099-353-3435', '010-34-34554', '342498765'
]
def test_good_cases():
    for s in good_numbers:
        mo = p.search(s)
        if not mo:
            print(f'Failed for goof numbers {s}')
        else:
            print(s, '-->', end='')
            if mo.group(3): #괄호 없는 지역번호, 폰번호 존재
                print(f'({mo.group(3)}) - {mo.group(5)} - {mo.group(6)}')
            elif mo.group(4): # 괄호 있는 지역번호, 폰번호 존재
                print(f'({mo.group(4)}) - {mo.group(5)} - {mo.group(6)}')
            else: #핸드폰 번호 간주
                print(mo.group(3),mo.group(4),mo.group(5),mo.group(6))

def test_bad_cases():
    for s in bad_numbers:
        mo = p.search(s)
        if mo:
            print(f'Failed for bad number {s} : {mo.group()}')
        else:
            print(f'{s} --> Wrong Number''')
def test_all():
    test_good_cases()
    test_bad_cases()





p.pattern #원래 정규식의 문자열이 그대로 들어있다.
pattern_str = re.sub(r'[ ]{2,}|\t|\n', '', p.pattern) #2개 이상의 연속된 공백, 탭, 개행 문자 삭제

import check_number as cn

for i in range(1000):
   cn.check(exrex.getone(pattern_str, 2))



