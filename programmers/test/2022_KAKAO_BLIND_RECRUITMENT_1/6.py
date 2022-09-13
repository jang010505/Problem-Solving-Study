def solution(board, skill):
    sum_board = [[0]*(len(board[i])+1) for i in range(len(board)+1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= 1

        sum_boardp[r1][c1] += degree
        sum_boardp[r2+1][c1] -= degree
        sum_boardp[r1][c2+1] -= degree
        sum_boardp[r2+1][c2+1] += degree

    for i in range(len(sum_board)):
        for j in range(1, len(sum_board[i])):
            dp[i][j] += dp[i][j-1]

    for i in range(1, len(sum_board)):
        for j in range(len(sum_board[i])):
            dp[i][j] += dp[i-1][j]

    answer = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] + sum_board[i][j] > 0:
                answer += 1
    return answer