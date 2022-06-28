def solution(n, m, board):
    answer = 0
    board = list(map(list, board))

    while True:
        lst = set()
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] != "-" and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    lst.add((i, j))
                    lst.add((i + 1, j))
                    lst.add((i, j + 1))
                    lst.add((i + 1, j + 1))

        if not lst:
            break

        answer += len(lst)

        for i, j in lst:
            board[i][j] = "-"

        for j in range(m):
            for _ in range(n):
                for i in range(n - 1, -1, -1):
                    if i - 1 >= 0 and board[i][j] == '-':
                        board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]

    return answer