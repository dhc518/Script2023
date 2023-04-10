import re

Local_Number = ['010', '02', '051', '053', '032', '062', '042', '052', '044', '031', '033', '043', '041', '063', '061', '054', '055', '064', None]

phone_re = re.compile(r'''
\(?(\d{2,3})?\)?    # 1그룹, 지역번호
\s?-?\s?            # separator
(\d{3,4})           # 2그룹, 중간 번호
\s?-?\s?            # separator
(\d{4})             # 3그룹, 뒷 번호
(\d*)               # 4그룹, 초과 숫자
''', re.VERBOSE)
def check(number):
    try:
        #mo = phone_re.search(input("Input Phone Number: "))
        mo = phone_re.search(number)
        mo.groups()
    except AttributeError as err: #그룹 입력 초과 또는 부족으로 인한 에러 (ex:010 - 34 - 34554)
        print(f'{number}    Wrong Number')
    else:
        if (len(mo.group()) == 10) and (mo.group()[:2] == '02'):#숫자가 10자리 이면서 앞에서 2자리가 02 인경우
            #print(f'({mo.group()[:2]}) {mo.group(1)[2]}{mo.group(2)} - {mo.group(3)}')
            pass
        elif mo.group(1) not in Local_Number: #첫 번째 그룹이 로컬 넘버에 포함되지 않는 경우
            print(f'{number}    Wrong Local Number')
        elif (mo.group(2)[0] == '0') or (len(mo.group(4))>0): #두번쨰 그룹이 0으로 시작하거나 숫자가 11자리를 초과한 경우
            print(f'{number}    Wrong Number')
        elif mo.group(1) == None: # 첫 번째 그룹에 아무것도 입력되지 않은 경우
            #print('(010)', end=' ')
            if (len(mo.group(3))<4): # 7자리인 경우
                #print(f'{mo.group(2)[:3]} - {mo.group(2)[3]}{mo.group(3)}')
                pass
            else: # 8자리인 경우
                #print(f'{mo.group(2)} - {mo.group(3)}')
                pass
        else: # 그 외
            #print(f'({mo.group(1)}) {mo.group(2)} - {mo.group(3)}')
            pass


