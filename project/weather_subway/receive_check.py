import csv
import os


def save(num, word_list, chat_id):
    filename = str(chat_id) +'.csv'
    # 파일이 이미 존재하는 경우
    if os.path.isfile(filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # 3번째 리스트의 내용 수정
        rows[num] = word_list

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    else:
        # 새로운 파일 생성
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            data = [[],[],[],[]]
            data[num] = word_list
            writer = csv.writer(file)
            writer.writerows(data)
    return '저장 되었습니다.'

def load(num, chat_id):
    filename = str(chat_id) +'.csv'
    # 파일이 이미 존재하는 경우
    if os.path.isfile(filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            try:
                word_list = ['오늘', rows[num][1], '날씨']
                word_list.append(rows[num+1][1])
                word_list.append(rows[num+1][2])
            except IndexError:
                return '저장을 잘못 하셨습니다.'
        return word_list
    else: return '저장된 데이터가 존재하지 않습니다.'

def check_text(text, chat_id):
    word_list = text.split()
    if word_list[0] == '.':
        print('미리 정한 지역의 날씨 및 지하철 데이터 1')
        word_list = load(0, chat_id)
        return word_list
    elif word_list[0] == '..':
        print('미리 정한 지역의 날씨 및 지하철 데이터 2')
        word_list = load(2, chat_id)
        return word_list
    elif word_list[0] == '오늘': #검색
        print('오늘 지역 날씨')
        word_list.append("날씨")
        return word_list
    elif word_list[0] == '내일': #검색
        print('내일 지역 날씨')
        word_list.append("날씨")
        return word_list
    elif word_list[0] == '금주': #검색
        print('오늘부터 7까지의 날씨')
        word_list.append("날씨")
        return word_list
    elif word_list[0] == '날씨1':  # 지역
        print('지역1 지정')
        return save(0, word_list, chat_id)
    elif word_list[0] == '역1':      #역이름
        print('역1 지정')
        return save(1, word_list, chat_id)
    elif word_list[0] == '날씨2':
        print('지역2 지정')
        return save(2, word_list, chat_id)
    elif word_list[0] == '역2': #역 이름
        print('역2 지정')
        return save(3, word_list, chat_id)
    else: return word_list


