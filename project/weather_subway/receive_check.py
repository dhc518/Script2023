def check_text(text):
    word_list = text.split()
    if word_list[0] == '.':
        print('미리 정한 지역의 날씨 및 지하철 데이터 1')
    elif word_list[0] == '..':
        print('미리 정한 지역의 날씨 및 지하철 데이터 2')
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
    elif word_list[0] == '':        # 호선, 역이름
        pass
    elif word_list[0] == '날씨1':     # 지역
        print('지역1 지정')
    elif word_list[0] == '역1':      #역이름
        print('역1 지정')
    elif word_list[0] == '날씨2':
        print('지역2 지정')
    elif word_list[0] == '역2': #역 이름
        print('역2 지정')


