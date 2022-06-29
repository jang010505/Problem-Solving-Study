def solution(cacheSize, cities):
    lst = list()

    answer = 0

    cities = [city.lower() for city in cities]

    for name in cities:
        if name in lst:
            lst.remove(name)
            lst.append(name)
            answer += 1
        else:
            answer += 5
            lst.append(name)
            if len(lst) > cacheSize:
                lst.pop(0)
    return answer