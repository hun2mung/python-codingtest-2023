# python-codingtest-2023
파이썬 코딩테스트 리포지토리

# 1일차
1. 코딩테스트 소개
2. 코딩테스트 학습
    - [x]자료구조
    - [x]배열 / 리스트
    - [x]구간합

# 2일차
1. 코딩테스트
    - [x]구간합 2
    - [x]자료구조 다시
        - 연결리스트
        - 스택
        - 큐
    - [x]파이썬 미리 구현된 스택, 큐, 기타 자료 구조 확인!

# 3일차
1. 코딩테스트 학습
    - 자료구조
        - [x]큐
        - [x]이진 트리
        - [x]그래프
        - [x]재귀호출
        - [x]정렬
        - [x]검색
        - [x]다이나믹 프로그래밍
# 4일차
1. 코딩테스트 학습
    - 자료구조
        - [x]그래프 계속
        - [x]재귀 호출
        - [x]정렬 소개

# 5일차
1. 코딩테스트 학습
    - 자료구조
        - [x]정렬
        - 검색
        - 다이나믹 프로그래밍

# 6일차
1. 코딩테스트 학습
    - 자료구조
        - [x]deque(덱)
    - 코딩테스트 알고리즘
        - 백준
        - 프로그래머스
```python
# 백준 11003 - 최솟값찾기 1
from collections import deque
# from pythonds.basic.deque import Deque

N, L = map(int, input().split())    # 12 3
mydeque = deque()
now = list(map(int, input().split()))   # 1 5 2 3 6 2 3 7 3 5 2 6

# 새 값이 들어올 때마다 정렬 대신 현재수보다 큰 값을 덱에서 제거
# 시간복잡도를 줄임

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:  # 인덱스가 현재값보다 크면
        mydeque.pop()   # 빼버린다
    mydeque.append((now[i],i))
    if mydeque[0][1] <= i - L:      # 범위를 벗어난 값도 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end = ' ')     # 무조건 최소값(min() 과 동일)


```