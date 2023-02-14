class Node():
    def __init__(self) -> None:
        self.data = None
        self.link = None

# 전역 변수
memory = []     #lists()
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

def printNodes(start):
    current = start
    if current == None:
        return

    print(current.data, end = ' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end=' -> ')

#노드 추가
def insertNode(findData, insertData):
    global memory, pre, current, head

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head  # 제일 앞으로
    while current.link != None:     # 중간 노드 삽입
        pre = current
        current = current.link

        if current.data ==findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # current.link == None 까지 온것
    node = Node()
    node.data = insertData
    current.link = node
    return

# 노드 삭제
def deleteNode(deleteData):
    global memory, pre, current, head

    if head.data == deleteData: # 첫 번째 노드 제거
        current = head
        head = head.link  # 두 번째 노드로 변경
        del(current)
        return
    
    current = head          #첫 번째 이외 노드 삭제
    while current.link != None: 
        pre = current # 모두 첫번째 노드 가르킴
        current = current.link  # 두 번째 노드를 가리킴
        if current.data == deleteData:
            pre.link = current.link # current 가리키는 노드를 pre가 가리키도록(삭제)
            del(current)
            return

# 노드 검색
def findNode(findData):
    global memory, pre, current, head
   
    current = head  # 첫 번째 노드부터
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link  # 다음 노드
        if current.data==findData:
            return current
    return Node()


if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0]    # 다현
    head = node
    memory.append(node)

    for data in dataArray[1:]:   # 두 번째 노드 이후
        pre = node
        node = Node()             
        node.data = data        # 정연, 쯔위, 지효, 사나
        pre.link = node
        memory.append(node)

    printNodes(head)    # 전체 출력

    print('---노드 추가---')

    insertNode('다현','화사')   # 맨 앞에 화사 노드 추가
    printNodes(head)
    insertNode('사나','솔라')   # 중간에 노드 추가
    printNodes(head)
    insertNode('재남','문별')   # 맨 마지막에 노드 추가
    printNodes(head)

    print('---노드 삭제---')

    deleteNode('화사')
    printNodes(head)
    deleteNode('지효')
    printNodes(head)
    deleteNode('재남')      # 데이터 없으므로 삭제 불가
    printNodes(head)

    print('---노드 검색---')
    
    result = findNode('정연')
    if result.data == '정연':
        print('데이터 찾았습니다')
    else:
        print('검색한 데이터 없습니다.')

    result = findNode('재남')
    print(result.data)