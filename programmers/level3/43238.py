def solution(n, times):
    times.sort()
    left = times[0]
    right = times[-1]*n

    while left < right:
        mid = (left+right)//2
        result = sum(map(lambda x: mid//x, times))
        if result < n:
            left = mid + 1
        else:
            right = mid

    return left