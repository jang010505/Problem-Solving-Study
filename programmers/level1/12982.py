def solution(d, budget):
    answer = 0
    d.sort()
    money = 0
    idx = 0
    while True:
        if idx >= len(d) or d[idx] + money > budget:
            break
        money += d[idx]
        answer += 1
        idx += 1

    return answer