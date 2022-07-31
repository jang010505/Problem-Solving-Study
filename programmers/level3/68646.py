def solution(a):
    result = [0 for _ in range(len(a))]
    minFront, minRear = 1e9, 1e9
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = 1
        if a[-1 - i] < minRear:
            minRear = a[-1 - i]
            result[-1 - i] = 1
    return sum(result)
