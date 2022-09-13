def dfs(info, edgeInfo, now, wolf, sheep, path):
    wolf += info[now]
    sheep += info[now] ^ 1

    if wolf >= sheep:
        return 0

    answer = sheep

    for p in path:
        for nxt in edgeInfo[p]:
            if nxt not in path:
                path.append(nxt)
                answer = max(answer, dfs(info, edgeInfo, nxt, wolf, sheep, path))
                path.pop()

    return answer


def solution(info, edges):
    edgeInfo = [[] for i in range(len(info) + 1)]
    for v, i in edges:
        edgeInfo[v].append(i)

    return dfs(info, edgeInfo, 0, 0, 0, [0])