n = 1024
answer = []
def solution(n):
    for i in range(2,n+1):
        if n%i == 0:
            result = n//i
            n = result
            answer.append(i)
            return solution(n)


if __name__ == '__main__':
    solution(n)
    print(list(set(answer)))