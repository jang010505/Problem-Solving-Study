def solution(n):
    lst = [[0] * n for i in range(n)]

    answer = []

    nowRow = 0
    nowCol = 0
    number = 1

    while n > 0:
        for i in range(n):
            lst[nowRow][nowCol] = number
            nowRow += 1
            number += 1

        nowRow -= 1

        for i in range(n - 1):
            nowCol += 1
            lst[nowRow][nowCol] = number
            number += 1

        for i in range(n - 2):
            nowCol -= 1
            nowRow -= 1
            lst[nowRow][nowCol] = number
            number += 1

        nowRow += 1
        n -= 3

    for l in lst:
        for num in l:
            if num:
                answer.append(num)

    return answer