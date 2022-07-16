def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree *= -1

        dp[r1][c1] += degree
        dp[r1][c2 + 1] -= degree
        dp[r2 + 1][c1] -= degree
        dp[r2 + 1][c2 + 1] += degree

    for i in range(N + 1):
        for j in range(1, M + 1):
            dp[i][j] += dp[i][j - 1]

    for i in range(1, N + 1):
        for j in range(M + 1):
            dp[i][j] += dp[i - 1][j]

    for i in range(N):
        for j in range(M):
            if board[i][j] + dp[i][j] > 0:
                answer += 1

    return answer