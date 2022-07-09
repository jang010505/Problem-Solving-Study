from collections import deque


def solution(board):
    N = len(board)
    dq = deque()
    visit = [[[1e9] * 4 for j in range(N)] for i in range(N)]
    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    visit[0][0][0] = 0
    visit[0][0][1] = 0
    visit[0][0][2] = 0
    visit[0][0][3] = 0

    dq.append([0, 0, 0])
    dq.append([0, 0, 1])
    dq.append([0, 0, 2])
    dq.append([0, 0, 3])
    while dq:
        now_i, now_j, vector = dq.popleft()

        for i in range(4):
            nxt_i = now_i + d[i][0]
            nxt_j = now_j + d[i][1]
            if 0 <= nxt_i < N and 0 <= nxt_j < N and board[nxt_i][nxt_j] == 0:
                if vector == i:
                    if visit[now_i][now_j][i] + 100 < visit[nxt_i][nxt_j][i]:
                        visit[nxt_i][nxt_j][i] = visit[now_i][now_j][i] + 100
                        dq.append([nxt_i, nxt_j, i])

                else:
                    if visit[now_i][now_j][vector] + 600 < visit[nxt_i][nxt_j][i]:
                        visit[nxt_i][nxt_j][i] = visit[now_i][now_j][vector] + 600
                        dq.append([nxt_i, nxt_j, i])

    return min(visit[-1][-1])