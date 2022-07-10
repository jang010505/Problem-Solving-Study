from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    for rect in rectangle:
        for i in range(4):
            rect[i] *= 2

    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    visit = [[0] * 101 for _ in range(101)]

    answer = 1e9

    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    dq = deque()
    dq.append([characterX, characterY, 0])
    visit[characterX][characterY] = 1
    check = [0] * len(rectangle)

    while dq:
        nowX, nowY, cnt = dq.popleft()

        if (nowX, nowY) == (itemX, itemY) and answer > cnt:
            answer = cnt

        for dx, dy in d:
            nxtX = nowX + dx
            nxtY = nowY + dy
            if 1 <= nxtX <= 100 and 1 <= nxtY <= 100:
                if not visit[nxtX][nxtY]:
                    for i, (startX, startY, endX, endY) in enumerate(rectangle):
                        if (nxtX < startX or nxtX > endX) or (nxtY < startY or nxtY > endY):
                            check[i] = -1
                        elif (startX < nxtX < endX) and (startY < nxtY < endY):
                            check[i] = -2
                            break
                        else:
                            check[i] = 1
                    if -2 in check or 1 not in check:
                        continue

                    visit[nxtX][nxtY] = 1
                    dq.append((nxtX, nxtY, cnt + 1))

    return answer // 2