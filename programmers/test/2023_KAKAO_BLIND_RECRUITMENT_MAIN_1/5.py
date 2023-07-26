from collections import deque


def unmerge(merge_info, shell, now):
    visit = [[0] * 51 for i in range(51)]
    r, c = now
    visit[r][c] = 1
    dq = deque()
    dq.append([r, c])

    while dq:
        now_r, now_c = dq.popleft()
        for nxt in merge_info[now_r][now_c]:
            nxt_r, nxt_c = nxt
            if visit[nxt_r][nxt_c] == 0:
                shell[nxt_r][nxt_c] = 0
                visit[nxt_r][nxt_c] = 1
                dq.append([nxt_r, nxt_c])
                merge_info[nxt_r][nxt_c].remove([now_r, now_c])

        merge_info[now_r][now_c] = []


def merge(merge_info, shell, target, now):
    visit = [[0] * 51 for i in range(51)]
    r, c = now
    visit[r][c] = 1
    dq = deque()
    dq.append([r, c])
    while dq:
        now_r, now_c = dq.popleft()
        shell[now_r][now_c] = target
        for nxt in merge_info[now_r][now_c]:
            nxt_r, nxt_c = nxt
            if visit[nxt_r][nxt_c] == 0:
                visit[nxt_r][nxt_c] = 1
                dq.append([nxt_r, nxt_c])


def solution(commands):
    answer = []

    shell = [[0] * 51 for _ in range(51)]
    merge_info = [[[] for j in range(51)] for i in range(51)]

    for command in commands:
        lst = list(command.split())
        if lst[0] == "UPDATE":
            if len(lst) == 3:
                cmd, value1, value2 = lst
                for i in range(1, 51):
                    for j in range(1, 51):
                        if shell[i][j] == value1:
                            shell[i][j] = value2
            else:
                cmd, r, c, value = lst
                r = int(r)
                c = int(c)
                shell[r][c] = value
                merge(merge_info, shell, value, [r, c])

        elif lst[0] == "MERGE":
            cmd, r1, c1, r2, c2 = lst
            r1 = int(r1)
            c1 = int(c1)
            r2 = int(r2)
            c2 = int(c2)
            merge_info[r1][c1].append([r2, c2])
            merge_info[r2][c2].append([r1, c1])
            target = 0
            if shell[r1][c1] == 0 and shell[r2][c2] != 0:
                target = shell[r2][c2]
            elif shell[r1][c1] != 0:
                target = shell[r1][c1]

            merge(merge_info, shell, target, [r1, c1])

        elif lst[0] == "UNMERGE":
            cmd, r, c = lst
            r = int(r)
            c = int(c)
            unmerge(merge_info, shell, [r, c])

        elif lst[0] == "PRINT":
            cmd, r, c = lst
            r = int(r)
            c = int(c)
            if shell[r][c] == 0:
                answer.append("EMPTY")
            else:
                answer.append(shell[r][c])

    return answer