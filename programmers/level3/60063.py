from collections import deque


def getNxtPos(pos, newBoard):
    nxtPos = []
    [x1, y1], [x2, y2] = pos
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for dx, dy in d:
        if newBoard[x1 + dx][y1 + dy] == 0 and newBoard[x2 + dx][y2 + dy] == 0:
            nxtPos.append({(x1 + dx, y1 + dy), (x2 + dx, y2 + dy)})

    if y1 == y2:
        for dy in [-1, 1]:
            if newBoard[x1][y1 + dy] == 0 and newBoard[x2][y2 + dy] == 0:
                nxtPos.append({(x1, y1), (x1, y1 + dy)})
                nxtPos.append({(x2, y2), (x2, y2 + dy)})
    else:
        for dx in [-1, 1]:
            if newBoard[x1 + dx][y1] == 0 and newBoard[x2 + dx][y2] == 0:
                nxtPos.append({(x1, y1), (x1 + dx, y1)})
                nxtPos.append({(x2, y2), (x2 + dx, y2)})

    return nxtPos


def solution(board):
    N = len(board)
    dq = deque()
    newBoard = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            newBoard[i][j] = board[i - 1][j - 1]

    pos = {(1, 1), (1, 2)}
    dq.append([pos, 0])
    visit = []
    visit.append(pos)

    while dq:
        pos, cost = dq.popleft()
        if (N, N) in pos:
            return cost

        for nxtPos in getNxtPos(pos, newBoard):
            if nxtPos not in visit:
                dq.append([nxtPos, cost + 1])
                visit.append(nxtPos)
