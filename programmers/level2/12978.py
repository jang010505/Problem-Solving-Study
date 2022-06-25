def solution(N, road, K):
    answer = 0

    info = [[1e9 for i in range(N+1)] for j in range(N+1)]

    for i in range(N+1):
        info[i][i] = 0

    for go, to, dist in road:
        info[go][to] = min(info[go][to], dist)
        info[to][go] = min(info[to][go], dist)

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                info[i][j] = min(info[i][k]+info[k][j], info[i][j])

    for i in range(1, N+1):
        if info[1][i] <= K:
            answer += 1


    return answer