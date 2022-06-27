def solution(brown, yellow):
    w = brown // 2 - 1
    for i in range(w, 2, -1):
        for j in range(i, 2, -1):
            if (i * j) == brown+yellow and (i-2)*(j-2) == yellow:
                return [i,  j]