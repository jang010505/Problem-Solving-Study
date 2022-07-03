def g(x, a):
    for i in range(x-1):
        if a[i] == a[x-1] or abs(a[i]-a[x-1])+1 == x-i:
            return False

    return True

def f(x, n, a):
    answer = 0
    if x == n:
        answer += 1
        return answer

    for i in range(n):
        a[x] = i
        if g(x+1, a):
            answer += f(x+1, n, a)

    return answer

def solution(n):
    return f(0, n, [-1]*n)