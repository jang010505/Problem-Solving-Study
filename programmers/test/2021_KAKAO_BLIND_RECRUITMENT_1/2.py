from itertools import combinations


def solution(orders, course):
    answer = []

    course_dict = dict()

    for order in orders:
        for count in course:
            for menu in combinations(order, count):
                menu = sorted(menu)
                menu = "".join(menu)
                if menu in course_dict:
                    course_dict[menu] += 1
                else:
                    course_dict[menu] = 1

    max_len = [2 for i in range(max(course) + 1)]
    max_str = [[] for i in range(max(course) + 1)]

    for key, value in course_dict.items():
        if max_len[len(key)] < value:
            max_len[len(key)] = value
            max_str[len(key)] = [key]
        elif max_len[len(key)] == value:
            max_str[len(key)].append(key)

    return sorted(sum(max_str, []))
