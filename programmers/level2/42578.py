def solution(clothes):
    clothesDict = dict()
    answer = 1

    for name, type in clothes:
        if type in clothesDict:
            clothesDict[type].append(name)
        else:
            clothesDict[type] = [name]

    for type in clothesDict.keys():
        answer *= (len(clothesDict[type]) + 1)

    return answer - 1