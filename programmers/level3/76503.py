import sys

sys.setrecursionlimit(10 ** 6)


def dfs(graph, visit, now, a):
    global answer
    result = a[now]
    visit[now] = 1
    for nxt in graph[now]:
        if visit[nxt] == 0:
            result += dfs(graph, visit, nxt, a)

    answer += abs(result)
    return result


def solution(a, edges):
    global answer
    answer = 0

    if sum(a):
        return -1

    graph = [[] for _ in range(len(a))]
    for v, i in edges:
        graph[v].append(i)
        graph[i].append(v)

    visit = [0] * len(a)
    dfs(graph, visit, 0, a)

    return answer