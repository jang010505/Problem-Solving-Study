def solution(n):
    answer = 0
    s = 0
    last = 0

    for i in range(1, n+1):
        if s + i <= n:
            s += i
            if s == n:
                answer += 1
        else:
            while s+i > n:
                s -= last
                last += 1

            s += i
            if s == n:
                answer += 1
    return answer