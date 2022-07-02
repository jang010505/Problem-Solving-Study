def solution(n):
    x = bin(n)[2:].count("1")
    n += 1
    y = bin(n)[2:].count("1")
    while x != y:
        n += 1
        y = bin(n)[2:].count("1")
    return n