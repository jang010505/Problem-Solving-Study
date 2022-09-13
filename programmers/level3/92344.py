def solution(board, skill):
    N = len(board)
    M = len(board[0])

    sum_board = [[0] * (M + 1) for _ in range(N + 1)]

    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree *= -1

        sum_board[r1][c1] += degree
        sum_board[r2 + 1][c1] -= degree
        sum_board[r1][c2 + 1] -= degree
        sum_board[r2 + 1][c2 + 1] += degree

    for i in range(N + 1):
        for j in range(1, M + 1):
            sum_board[i][j] += sum_board[i][j - 1]

    for i in range(1, N + 1):
        for j in range(M + 1):
            sum_board[i][j] += sum_board[i - 1][j]

    answer = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] + sum_board[i][j] > 0:
                answer += 1

    return answer