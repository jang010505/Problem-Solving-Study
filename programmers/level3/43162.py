from collections import deque

def solution(n, computers):
    visit = [0] * n

    nodeInfo = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                nodeInfo[i].append(j)

    answer = 0
    for i in range(n):
        if visit[i] == 0:
            answer += 1
            visit[i] = 1
            dq = deque()
            dq.append(i)
            while dq:
                now = dq.popleft()
                for nxt in nodeInfo[now]:
                    if visit[nxt] == 0:
                        visit[nxt] = 1
                        dq.append(nxt)


    return answer