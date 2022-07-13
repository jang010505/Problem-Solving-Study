import sys
sys.setrecursionlimit(10**6)

def dfs(info, nodeInfo, sheep, wolf, now, path):
    if info[now]:
        wolf += 1
    else:
        sheep += 1

    if sheep <= wolf:
        return 0

    result = sheep

    for p in path:
        for nxt in nodeInfo[p]:
            if nxt not in path:
                path.append(nxt)
                result = max(result, dfs(info, nodeInfo, sheep, wolf, nxt, path))
                path.pop()

    return result



def solution(info, edges):
    nodeInfo = [[] for _ in range(len(edges)+1)]

    for v, i in edges:
        nodeInfo[v].append(i)

    return dfs(info, nodeInfo, 0, 0, 0, [0])