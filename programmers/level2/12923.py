def f(n):
    if n == 1:
        return 0

    i = max(2, n//10000000)
    while i*i <= n:
        if n%i == 0 and n/i <= 10000000:
            return n//i
        i += 1

    return 1

def solution(begin, end):
    answer = []

    for i in range(begin, end+1):
        answer.append(f(i))

    return answer