def solution(n, s, a, b, fares):
    floyd = [[1e9] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        floyd[i][i] = 0

    for go, to, dist in fares:
        floyd[go][to] = dist
        floyd[to][go] = dist

    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

    answer = 1e9
    for i in range(1, n + 1):
        answer = min(answer, floyd[s][i] + floyd[i][a] + floyd[i][b])

    return answer