def solution(n):
    if n**(0.5) == int(n**(0.5)):
        return pow(int(n**(0.5))+1, 2)
    else:
        return -1