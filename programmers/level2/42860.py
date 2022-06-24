def selectLen(key, target):
    return min(abs(ord(key) - ord(target)), 26 - abs(ord(key) - ord(target)))


def func(posList, nowPos, length, visit):
    global distance
    if sum(visit) == len(visit):
        distance = min(distance, length)
        return

    for i in posList:
        if visit[i] == 0:
            visit[i] = 1
            dist = min(abs(nowPos - i), len(visit) - abs(nowPos - i))
            func(posList, i, length + dist, visit)
            visit[i] = 0


def solution(name):
    answer = 0
    N = len(name)

    global distance
    distance = 10e9

    posList = list()
    visit = [0 for i in range(N)]

    for i, x in enumerate(name):
        if x != "A":
            posList.append(i)
            answer += selectLen(x, "A")
        else:
            visit[i] = 1

    func(posList, 0, 0, visit)

    return answer + distance