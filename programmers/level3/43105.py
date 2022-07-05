def solution(triangle):
    answer = 0
    dp = [[0]*len(triangle) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]

    return max(dp[-1])