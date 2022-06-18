def solution(a, b):
    answer = 0
    for numA, numB in zip(a, b):
        answer += a*b
    return answer