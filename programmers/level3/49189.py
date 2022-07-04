import heapq

def solution(n, edge):
    nodeInfo = [[] for i in range(n+1)]

    for go, to in edge:
        nodeInfo[go].append(to)
        nodeInfo[to].append(go)

    distance = [1e9]*(n+1)

    distance[1] = 0
    q = []
    heapq.heappush(q, [0, 1])

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] >= dist:
            for n in nodeInfo[now]:
                cost = dist + 1
                if cost < distance[n]:
                    distance[n] = cost
                    heapq.heappush(q, [cost, n])

    return distance.count(max(distance[1:]))