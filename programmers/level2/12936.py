def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n

def solution(n, k):
    answer = []
    lst = [i for i in range(1, n+1)]

    while n != 0:
        s = factorial(n)//n
        now = (k-1)//s
        answer.append(lst[now])
        lst.remove(lst[now])
        n -= 1
        k %= s
        if k == 0:
            k = s
    return answer