def isPrime(n):
    if n == 1:
        return 0

    i = 2
    while i*i <= n:
        if n%i == 0:
            return 0

        i += 1

    return 1

def solution(n, k):
    number = ""

    while n:
        number = str(n%k) + number
        n //= k

    number_lst = number.split("0")

    answer = 0

    for s in number_lst:
        try:
            num = int(s)
            if isPrime(num):
                answer += 1
        except:
            continue

    return answer