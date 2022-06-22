from itertools import combinations


def solution(orders, course):
    courseDict = dict()

    max_len = [2 for i in range(max(course) + 1)]
    max_str = [[] for i in range(max(course) + 1)]

    for order in orders:
        for num in course:
            for menu in combinations(order, num):
                menu = sorted(menu)
                menu = "".join(menu)
                if menu in courseDict:
                    courseDict[menu] += 1
                else:
                    courseDict[menu] = 1

    for key, value in courseDict.items():
        if max_len[len(key)] < value:
            max_len[len(key)] = value
            max_str[len(key)] = [key]
        elif max_len[len(key)] == value:
            max_str[len(key)].append(key)

    answer = sorted(sum(max_str, []))

    return answer