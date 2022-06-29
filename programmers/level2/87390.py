def solution(n, left, right):
    return [i%n+max(0, i//n - i%n)+1 for i in range(left, right+1)]