def f(N):
    count = 0
    for i in range(1, N+1):
        if N%i == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0

    for i in range(left, right +1):
        if f(i)%2:
            answer -= i
        else:
            answer += i
    return answer