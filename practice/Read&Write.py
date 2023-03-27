# File_Name 과 Path
# File_Name
#     파일의 이름과 확장자로 구성
# Path
#     컴퓨터에서 파일의 위치를 가리킴
# 폴더 이름 구분
#     Windows : \\
#     Linux, Mac : /

# Absolute path
#     Root 폴더로 시작, 윈도우의 경우 드라이버 문자에서 시작
# Relative path
#     특정 위치를 기준으로 한 경로
#     일반적으로 cwd 가 기준
#     배포하려면 상대 경로를 써야 한다.
#     . : 현재 폴더
#     .. : 상위 폴더


import os

# os.path.join('usr', 'bin', 'spam')
#
# os.getcwd() #실행 폴더 경로
# os.chdir('C:/Windows/System32') #경로 변경
# os.getcwd() #'C:\\Windows\\System32'

# os.path.abspath('.')# 상대경로
# os.listdir()        # 폴더 리스트
# os.mkdir('sub')     # 폴더 생성
# os.path.abspath('./sub')# 상대경로
# os.path.isabs('.')  # 절대경로이냐? False
# os.path.isabs('w:/workCoding')# True
# os.path.relpath('w:/workCoding','w:/workCoding/2022-Script-Language')# 상대경로 표시
# # '..'
# os.path.relpath('w:/workCoding/2022-Script-Language','w:/workCoding')
# # '2022-Script-Language'

# 새 폴더 만들기
# os.mkdir('폴더명') #현재 폴더에서만 만들 수 있음
# os.makedirs('경로 및 폴더명')

# Dir Name, Base Name
# os.path.basename()
# os.path.dirname()
# os.path.split()     #배이스와 디렉토리 분리
# os.path.splitext()  #확장자와 경로 분리

#Path 유효성 검증
# os.path.exists()
# os.path.isdir()
# os.path.isfile()

#폴더 전체 구조 탐사


#Shelve 모듈
    # 모든 변수들은 파일로 기록하고(Serialization), 읽을(de-serialization) 수 있음.
    # 딕셔너리 형태로 액세스
# import shelve
# import random
# data = [random.randint(0,100) for i in range(100)]
# data_file = shelve.open('mydata')
# data_file['data'] = data
# data_file.close()
# f = shelve.open('mydata')
# data = f['data']

#Dictionary sort
# def get_key(x):
#     return x[1]
# data = {'jisu':100, 'momo':20, 'rose':200, 'iu':3}
# result = sorted(data.items(), key=get_key, reverse=True)
# # lambda 함수 사용
# result = sorted(data.items(), key=lambda x: x[1], reverse=True)

