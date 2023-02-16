def openBox():
    global count
    print('종이 상자를 엽니다. ^^')
    count -= 1
    if count == 0:
        print('** 반지를 넣고 반환합니다. **')
        return  # 호출한 함수 위치로 복귀
    print(count)
    openBox()
    print(count)
    print('종이 상자를 닫습니다. ^^')

count = 3
openBox()