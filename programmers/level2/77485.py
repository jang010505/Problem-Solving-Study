def solution(rows, columns, queries):
    info = [[columns * i + j for j in range(1, columns + 1)] for i in range(rows)]
    answer = []
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        prevNum = info[x1 + 1][y1]
        nowNum = info[x1][y1]

        minValue = prevNum

        for dy in range(y1, y2 + 1):
            nowNum = info[x1][dy]
            minValue = min(minValue, nowNum)
            info[x1][dy] = prevNum
            prevNum = nowNum

        for dx in range(x1 + 1, x2 + 1):
            nowNum = info[dx][y2]
            minValue = min(minValue, nowNum)
            info[dx][y2] = prevNum
            prevNum = nowNum

        for dy in range(y2-1, y1-1, -1):
            nowNum = info[x2][dy]
            minValue = min(minValue, nowNum)
            info[x2][dy] = prevNum
            prevNum = nowNum

        for dx in range(x2-1, x1-1, -1):
            nowNum = info[dx][y1]
            minValue = min(minValue, nowNum)
            info[dx][y1] = prevNum
            prevNum = nowNum

        answer.append(minValue)

    return answer