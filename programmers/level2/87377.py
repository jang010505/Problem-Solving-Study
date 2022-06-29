def position(A, B, E, C, D, F):
    AD_BC = A * D - B * C

    if AD_BC == 0:
        return 0

    return ((B * F - E * D) / (AD_BC), (E * C - A * F) / (AD_BC))


def solution(line):
    lst = list()

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            A, B, C = line[i]
            D, E, F = line[j]
            x = position(A, B, C, D, E, F)
            if x == 0:
                continue
            else:
                if int(x[0]) == x[0] and int(x[1]) == x[1]:
                    lst.append([int(x[0]), int(x[1])])

    lst = list(lst)

    lst = sorted(lst, key=lambda x: x)

    max_row = lst[0][1]
    min_row = lst[0][1]
    max_col = lst[-1][0]
    min_col = lst[0][0]

    for i in range(1, len(lst)):
        max_row = max(max_row, lst[i][1])
        min_row = min(min_row, lst[i][1])

    row = abs(max_row - min_row) + 1
    col = abs(max_col - min_col) + 1

    answer = [["."] * col for i in range(row)]

    if min_row != 0:
        min_row *= -1
    else:
        min_row = 0

    if min_col != 0:
        min_col *= -1
    else:
        min_col = 0

    for i in range(len(lst)):
        lst[i][0] += min_col
        lst[i][1] += min_row

    for j, i in lst:
        answer[row - i - 1][j] = "*"

    return ["".join(l) for l in answer]