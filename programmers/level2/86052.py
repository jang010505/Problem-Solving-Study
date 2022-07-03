import sys

sys.setrecursionlimit(600000)


def f(nowRow, nowCol, pos, visit, grid, N, M):
    nxtCol = nowCol
    nxtRow = nowRow
    result = 0
    if grid[nowRow][nowCol] == "S":
        if pos == 0:
            nxtCol += 1
        elif pos == 1:
            nxtRow += 1
        elif pos == 2:
            nxtCol -= 1
        else:
            nxtRow -= 1

    elif grid[nowRow][nowCol] == "R":
        if pos == 0:
            nxtRow += 1
        elif pos == 1:
            nxtCol -= 1
        elif pos == 2:
            nxtRow -= 1
        else:
            nxtCol += 1

        pos = (pos + 1) % 4

    elif grid[nowRow][nowCol] == "L":
        if pos == 0:
            nxtRow -= 1
        elif pos == 1:
            nxtCol += 1
        elif pos == 2:
            nxtRow += 1
        else:
            nxtCol -= 1

        pos = (pos - 1) % 4

    nxtRow %= N
    nxtCol %= M

    if visit[nxtRow][nxtCol][pos] == 1:
        return result

    visit[nxtRow][nxtCol][pos] = 1
    result += f(nxtRow, nxtCol, pos, visit, grid, N, M) + 1

    return result


def solution(grid):
    row = len(grid)
    col = len(grid[0])

    answer = []
    visit = [[[0] * 4 for j in range(col)] for i in range(row)]

    for i in range(row):
        for j in range(col):
            for k in range(4):
                if visit[i][j][k] == 0:
                    visit[i][j][k] = 1
                    answer.append(f(i, j, k, visit, grid, row, col) + 1)

    return sorted(answer)