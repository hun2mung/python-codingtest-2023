# 프로그래머스 템플릿 소스

# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = 0
    for i in numbers:
        answer+=i
    return answer / len(numbers)

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(solution(numbers))
    
    numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    print(solution(numbers))