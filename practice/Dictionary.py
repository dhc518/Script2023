student = {'name':'Tom', 'grade' : 'A+'} # 초기화
student['name']
student['height'] = 178.5 # key, value를 넣는 방법
student['grade']

##############keys(), values(), items()############
student.get('name')
student.get('address')
student.get('address', 'AAA')
student.setdefault('color', 'black')
student.setdefault('color', 'white')# 키가 없으면 지정, 키가 있으면 무시
student['color']