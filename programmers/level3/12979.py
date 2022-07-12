def solution(n, stations, w):
    answer = 0

    stations = sorted(stations)

    for i in range(len(stations)):
        if i == 0:
            x = stations[i] - w - 1
            if x >= 0:
                answer += x // (2 * w + 1)
                if x % (2 * w + 1):
                    answer += 1

        if i == len(stations) - 1:
            x = n - (stations[i] + w)
            if x >= 0:
                answer += x // (2 * w + 1)
                if x % (2 * w + 1):
                    answer += 1
        else:
            x = stations[i + 1] - stations[i] - 2 * w - 1
            if x >= 0:
                answer += x // (2 * w + 1)
                if x % (2 * w + 1):
                    answer += 1

    return answer