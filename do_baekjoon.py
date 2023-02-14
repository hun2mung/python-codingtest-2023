def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return print(answer)

solution([1, 2, 3, 4, 5])

# from fractions import Fraction

# def solution(numer1, denom1, numer2, denom2):

#     a = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    
#     answer = [a.numerator, a.denominator]

#     return answer

# solution(9,2,1,3)

# def solution(numbers):
#     answer = [x*2 for x in numbers]
#     return answer