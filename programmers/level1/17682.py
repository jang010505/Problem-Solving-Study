def solution(dartResult):
    i = 0
    l = len(dartResult)

    answer = 0

    prevScore = 0
    nowScore = 0

    while i < l:
        prevScore = nowScore
        number = 0
        while '0' <= dartResult[i] <= '9':
            number = number*10 + int(dartResult[i])
            i += 1
        power = dartResult[i]
        option = ""
        if i + 1 < l and (dartResult[i + 1] == "*" or dartResult[i + 1] == "#"):
            option = dartResult[i + 1]
            i += 2
        else:
            i += 1

        if power == "S":
            power = 1
        elif power == "D":
            power = 2
        elif power == "T":
            power = 3
        else:
            return 0

        nowScore = number ** power

        if option == "*":
            prevScore *= 2
            nowScore *= 2
        elif option == "#":
            nowScore *= -1

        answer += prevScore

    answer += nowScore

    return answer