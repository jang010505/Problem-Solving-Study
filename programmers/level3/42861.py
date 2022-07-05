def find(p, u):
    if u != p[u]:
        p[u] = find(p, p[u])
    return p[u]


def union(p, u, v):
    root1 = find(p, u)
    root2 = find(p, v)
    p[root2] = root1


def solution(n, costs):
    answer = 0
    m = 0
    costs = sorted(costs, key=lambda x: x[2])
    p = [i for i in range(n)]

    while m < n - 1:
        u, v, w = costs.pop(0)
        if find(p, u) != find(p, v):
            union(p, u, v)
            m += 1
            answer += w

    return answer
