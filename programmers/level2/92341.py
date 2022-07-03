def timeChange(s):
    h, m = map(int, s.split(":"))
    return h * 60 + m


def feeCumpute(fees, totalTime):
    result = 0
    result += fees[1]
    if totalTime > fees[0]:
        totalTime -= fees[0]
        if totalTime % fees[2]:
            result += fees[3] * (totalTime // fees[2] + 1)
        else:
            result += fees[3] * (totalTime // fees[2])
    return result


def solution(fees, records):
    answer = []

    recordDict = dict()

    for record in records:
        time, number, state = record.split()
        if number in recordDict:
            if recordDict[number][1] == "IN":
                recordDict[number][2] += timeChange(time) - recordDict[number][0]
            else:
                recordDict[number][0] = timeChange(time)

            recordDict[number][1] = state
        else:
            recordDict[number] = [timeChange(time), state, 0]

    for key in recordDict.keys():
        if recordDict[key][1] == "IN":
            recordDict[key][2] += timeChange("23:59") - recordDict[key][0]
            recordDict[key][1] = "OUT"

    answer = sorted([[number, feeCumpute(fees, item[2])] for number, item in recordDict.items()], key=lambda x: x[0])

    return [x for _, x in answer]