def dfs(board, nowloc, nxtloc):
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    answer = 0
    nowX, nowY = nowloc
    if board[nowX][nowY] == 0:
        return 0

    for dx, dy in d:
        nxtX = dx + nowX
        nxtY = dy + nowY

        if 0 <= nxtX < len(board) and 0 <= nxtY < len(board[0]):
            if board[nxtX][nxtY]:
                board[nowX][nowY] = 0
                result = dfs(board, nxtloc, [nxtX, nxtY]) + 1
                board[nowX][nowY] = 1

                if answer % 2 == 0 and result % 2:
                    answer = result
                elif answer % 2 == 0 and result % 2 == 0:
                    answer = max(answer, result)
                elif answer % 2 and result % 2:
                    answer = min(answer, result)

    return answer


def solution(board, aloc, bloc):
    return dfs(board, aloc, bloc)