def solution(n, results):
    nodeInfo = [[0] * n for _ in range(n)]

    for win, lose in results:
        nodeInfo[win - 1][lose - 1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if nodeInfo[i][j] or (nodeInfo[i][k] and nodeInfo[k][j]):
                    nodeInfo[i][j] = 1

    answer = [0] * n
    for i in range(n):
        for j in range(n):
            if nodeInfo[i][j] == 1:
                answer[i] += 1
                answer[j] += 1

    return answer.count(n - 1)