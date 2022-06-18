def solution(numbers, hand):
    rightPosition = "#"
    leftPosition = "*"

    answer = ''

    numberPosition = dict()
    numberPosition[1] = [1, 1]
    numberPosition[2] = [1, 2]
    numberPosition[3] = [1, 3]
    numberPosition[4] = [2, 1]
    numberPosition[5] = [2, 2]
    numberPosition[6] = [2, 3]
    numberPosition[7] = [3, 1]
    numberPosition[8] = [3, 2]
    numberPosition[9] = [3, 3]
    numberPosition["*"] = [4, 1]
    numberPosition[0] = [4, 2]
    numberPosition["#"] = [4, 3]

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            leftPosition = number
        elif number in [3, 6, 9]:
            answer += "R"
            rightPosition = number
        else:
            numPos = numberPosition[number]
            lPos = numberPosition[leftPosition]
            rPos = numberPosition[rightPosition]
            lLength = abs(lPos[0]-numPos[0])+abs(lPos[1]-numPos[1])
            rLength = abs(rPos[0]-numPos[0])+abs(rPos[1]-numPos[1])
            if lLength == rLength:
                if hand == "left":
                    answer += "L"
                    leftPosition = number
                else:
                    answer += "R"
                    rightPosition = number
            elif lLength < rLength:
                answer += "L"
                leftPosition = number
            else:
                answer += "R"
                rightPosition = number
    return answer