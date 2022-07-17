from collections import deque

def solution(A, B):
    answer = 0
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    dq = deque()

    for x in B:
        dq.append(x)

    for x in A:
        y = dq.popleft()
        if x < y:
            answer += 1
        else:
            dq.appendleft(y)
            dq.pop()

    return answer