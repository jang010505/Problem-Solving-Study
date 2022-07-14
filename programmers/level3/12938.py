def solution(n, s):
    answer = []
    base = s // n
    rem = s % n

    if base == 0:
        return [-1]

    for _ in range(n - rem):
        answer.append(base)
    for _ in range(rem):
        answer.append(base + 1)

    return answer