from collections import deque

def solution(priorities, location):
    printWhen = [0 for i in range(len(priorities))]

    dq = deque()

    for i, task in enumerate(priorities):
        dq.append([task, i])

    count = 1

    while dq:
        front, pos = dq.popleft()
        if dq and front < max(dq)[0]:
            dq.append([front, pos])
        else:
            printWhen[pos] = count
            count += 1

    return printWhen[location]