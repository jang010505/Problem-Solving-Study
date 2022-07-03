from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def solution(arr):
    answer = arr[0]
    for x in arr[1:]:
        answer = lcm(answer, x)

    return answer