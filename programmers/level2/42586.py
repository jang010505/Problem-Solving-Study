def solution(progresses, speeds):
    info = [0] * len(progresses)

    for i, element in enumerate(zip(progresses, speeds)):
        a, b = element
        if (100 - a) % b == 0:
            info[i] = (100 - a) // b
        else:
            info[i] = (100 - a) // b + 1

    answer = []
    result = 1
    prevDay = info[0]

    for nowDay in info[1:]:
        if prevDay >= nowDay:
            result += 1
        else:
            answer.append(result)
            result = 1
            prevDay = nowDay

    answer.append(result)

    return answer