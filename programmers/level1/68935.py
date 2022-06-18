def solution(n):
    result = ""
    while n != 0:
        result += str(n % 3)
        n //= 3

    answer = int(result, 3)
    return answer