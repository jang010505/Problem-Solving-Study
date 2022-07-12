def solution(n, cores):
    answer = 0

    if n <= len(cores):
        return n

    n -= len(cores)

    left = 0
    right = n * max(cores)

    while left < right:
        mid = (left + right) // 2
        result = sum(map(lambda x: mid // x, cores))
        if result < n:
            left = mid + 1
        else:
            right = mid

    for c in cores:
        n -= (right - 1) // c

    for i, core in enumerate(cores):
        if right % core == 0:
            n -= 1
            if n == 0:
                return i + 1