def solution(sizes):
    dp = [[0]*len(sizes) for i in range(len(sizes))]

    for i in range(1, len(sizes)):
        for s in range(0, len(sizes) - i):
            e = s + i

            x = list()
            for m in range(s, e):
                x.append(dp[s][m] + dp[m + 1][e] + sizes[s][0] * sizes[m][1] * sizes[e][1])
            dp[s][e] = min(x)

    return dp[0][-1]
