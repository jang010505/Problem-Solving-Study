def change(N, x):
    result = ""
    while N > 0:
        result = str(N % x) + result
        N //= x

    if len(result) == 0:
        result = "0"

    return result


def isPrime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def solution(n, k):
    lst = list(change(n, k).split("0"))
    result = list()
    for element in lst:
        if len(element):
            result.append(int(element))

    answer = 0

    for number in result:
        if isPrime(number):
            answer += 1
    return answer