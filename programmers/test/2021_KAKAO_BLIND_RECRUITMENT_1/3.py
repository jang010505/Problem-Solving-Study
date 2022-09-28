def solution(n, s, a, b, fares):
    answer = 1e9
    inf = 1e9

    floyd = [[0 if i == j else inf for j in range(n + 1)] for i in range(n + 1)]

    for go, to, cost in fares:
        floyd[go][to] = cost
        floyd[to][go] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

    for i in range(1, n + 1):
        answer = min(answer, floyd[s][i] + floyd[i][a] + floyd[i][b])

    return answer