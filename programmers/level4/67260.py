from collections import deque


def solution(n, path, order):
    answer = True
    graph = {n: [] for n in range(n)}

    for x, y in path:
        graph[x].append(y)
        graph[y].append(x)

    precedeA = {}
    precedeB = {}

    for a, b in order:
        precedeA[a] = b
        precedeB[b] = a
        if b == 0:
            return False

        if a == 0:
            precedeA[0] = 0

    visit = [0] * n
    visit[0] = 1

    q = deque()
    q.append(0)

    while q:
        now = q.popleft()

        if now == precedeA.get(precedeB.get(now)):
            visit[now] = 2
        else:
            for x in graph[now]:
                if visit[x] == 0:
                    q.append(x)
                    visit[x] = 1

                    if precedeA.get(x):
                        if visit[precedeA[x]] == 2:
                            q.append(precedeA[x])
                            visit[precedeA[x]] = 1

                        precedeA[x] = 0

    for i in visit:
        if i == 0:
            return False

    return answer