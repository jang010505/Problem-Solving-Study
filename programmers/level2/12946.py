def hanoi(n, go, tmp, to):
    global answer
    if n == 1:
        answer.append([go, to])
    else:
        hanoi(n-1, go, to, tmp)
        answer.append([go, to])
        hanoi(n-1, tmp, go, to)


def solution(n):
    global answer
    answer = []
    hanoi(n, 1, 2, 3)
    return answer