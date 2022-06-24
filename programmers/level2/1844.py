from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])

    distance = [[9999 for i in range(M)] for j in range(N)]

    distance[0][0] = 1
    dq = deque()

    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    dq.append([0, 0])

    while dq:
        now_x, now_y = dq.popleft()
        cost = distance[now_x][now_y]

        for dx, dy in d:
            nxt_x = now_x + dx
            nxt_y = now_y + dy

            if 0 <= nxt_x < N and 0 <= nxt_y < M:
                if maps[nxt_x][nxt_y] == 1 and cost + 1 < distance[nxt_x][nxt_y]:
                    distance[nxt_x][nxt_y] = cost + 1
                    dq.append([nxt_x, nxt_y])

    if distance[-1][-1] == 9999:
        return -1

    return distance[-1][-1]