from collections import deque


def solution(k, dungeons):
    dq = deque()
    answer = 0
    N = len(dungeons)
    dq.append([k, []])
    while dq:
        p, v = dq.popleft()
        for i in range(N):
            [a, b] = dungeons[i]
            if i not in v and p >= a and p - b >= 1:
                dq.append([p - b, v + [i]])
            else:
                answer = max(answer, len(v))
    return answer
