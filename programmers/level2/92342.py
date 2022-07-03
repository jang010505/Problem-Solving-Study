def f(x, n, info1, info2):
    global answer, maxValue
    if x == 0:
        if n > 0:
            info2[x] = n
        else:
            info2[x] = 0

        score1 = 0
        score2 = 0
        i = 0
        for x, y in zip(info1, info2):
            if x == y == 0:
                i += 1
                continue
            elif x < y:
                score2 += i
            else:
                score1 += i
            i += 1

        if score1 < score2:
            if maxValue < abs(score1 - score2):
                answer = list(reversed(info2))
                maxValue = abs(score1 - score2)
            elif maxValue == abs(score1 - score2):
                check = True
                for x, y in zip(reversed(answer), info2):
                    if x > y:
                        check = False
                        break
                    elif x < y:
                        break
                if check:
                    answer = list(reversed(info2))
    else:
        info2[x] = 0
        f(x - 1, n, info1, info2)
        if n - info1[x] - 1 >= 0:
            info2[x] = info1[x] + 1
            f(x - 1, n - info1[x] - 1, info1, info2)


def solution(n, info):
    global answer, maxValue
    answer = [-1]
    maxValue = 0
    f(10, n, list(reversed(info)), [0] * 11)
    return answer