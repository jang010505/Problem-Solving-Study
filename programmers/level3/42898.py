def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]

    dp[0][0] = 1
    puddles = list(map(tuple, puddles))
    puddles = set(puddles)

    for i in range(n):
        for j in range(m):
            if i == 0:
                if j == 0:
                    continue
                elif (j+1, i+1)not in puddles:
                    dp[i][j] = dp[i][j - 1]
            elif (j+1, i+1) not in puddles:
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i][j-1])%1000000007

    return dp[-1][-1]