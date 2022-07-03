def changeTime(time):
    h, m, s = map(float, time.split(":"))
    return h * 3600 + m * 60 + s


def solution(lines):
    answer = 1

    for i in range(len(lines) - 1):
        _, time_i, s_i = lines[i].split()
        endTime_i = changeTime(time_i)
        startTime_i = endTime_i - float(s_i[:-1]) + 0.001
        result = 1
        for j in range(i + 1, len(lines)):
            _, time_j, s_j = lines[j].split()
            endTime_j = changeTime(time_j)
            startTime_j = endTime_j - float(s_j[:-1]) + 0.001

            if endTime_i > startTime_j-1:
                result += 1

        answer = max(answer, result)

    return answer
