def isPrime(n):
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def func(numbers, s, visit):
    global answer
    global primeSet

    if len(s) > 0 and isPrime(int(s)):
        if int(s) not in primeSet:
            primeSet.add(int(s))
            answer += 1

    for i in range(len(numbers)):
        if visit[i] == 0:
            visit[i] = 1
            func(numbers, s + numbers[i], visit)
            visit[i] = 0


def solution(numbers):
    global answer, primeSet
    answer = 0
    primeSet = set()
    visit = [0 for i in range(len(numbers))]
    func(numbers, "", visit)
    return answer