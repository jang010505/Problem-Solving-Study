def compute(n):
    s = ""
    while n:
        s = str(n % 2) + s
        n //= 2

    d = [pow(2, n) - 1 for n in range(1, 64)]
    while True:
        if len(s) in d:
            break
        else:
            s = '0' + s

    return s


def f(x):
    global check
    if len(x) == 1:
        return

    if x[len(x) // 2] == "0":
        if x[len(x) // 2 + (len(x) // 2 + 1) // 2] == "1" or x[len(x) // 2 - (len(x) // 2 + 1) // 2] == "1":
            check = False
        f(x[:len(x) // 2])
        f(x[len(x) // 2 + 1:])
    else:
        f(x[:len(x) // 2])
        f(x[len(x) // 2 + 1:])


def solution(numbers):
    answer = []
    for x in numbers:
        global check
        check = True
        f(compute(x))
        if check:
            answer.append(1)
        else:
            answer.append(0)
    return answer