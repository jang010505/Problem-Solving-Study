from collections import deque


def solution(n, wires):
    info = [[] * (n + 1) for _ in range(n + 1)]
    answer = n
    for go, to in wires:
        info[go].append(to)
        info[to].append(go)

    for x, y in wires:
        info[x].remove(y)
        info[y].remove(x)

        count1 = 1
        count2 = 1

        dq = deque()
        dq.append(x)
        visit = [0] * (n + 1)
        visit[x] = 1

        while dq:
            now = dq.popleft()
            for nxt in info[now]:
                if not visit[nxt]:
                    visit[nxt] = 1
                    dq.append(nxt)
                    count1 += 1

        dq.append(y)
        visit = [0] * (n + 1)
        visit[y] = 1

        while dq:
            now = dq.popleft()
            for nxt in info[now]:
                if not visit[nxt]:
                    visit[nxt] = 1
                    dq.append(nxt)
                    count2 += 1
        info[x].append(y)
        info[y].append(x)
        answer = min(answer, abs(count1 - count2))

    return answer