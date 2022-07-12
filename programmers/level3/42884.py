def solution(routes):
    answer = 0

    routes = sorted(routes, key=lambda x: x[1])

    result = -30001

    for x, y in routes:
        if result < x:
            answer += 1
            result = y


    return answer