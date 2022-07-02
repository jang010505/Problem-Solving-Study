def change(N, x):
    result = ""
    while N > 0:
        if N % x < 10:
            result = str(N%x) + result
        else:
            result = chr(N%x-10+65) + result
        N //= x

    if len(result) == 0:
        result = "0"

    return result


def solution(n, t, m, p):
    answer = []
    result = ""
    now = 0
    while len(result) < t*m:
        result += change(now, n)
        now += 1

    now = p-1
    while len(answer) < t:
        answer.append(result[now])
        now += m

    return "".join(answer)