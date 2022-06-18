def solution(n):
    n -= 1
    answer = 2
    while n % answer != 0:
        answer += 1
    return answer