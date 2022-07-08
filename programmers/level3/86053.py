def solution(a, b, g, s, w, t):
    answer = (1e9) * (1e5) * 4
    start = 0
    end = (1e9) * (1e5) * 4

    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0

        for nowGold, nowSilver, nowWeight, nowTime in zip(g, s, w, t):
            count = mid // (nowTime * 2)

            if mid % (nowTime * 2) >= nowTime:
                count += 1

            if nowGold < count * nowWeight:
                gold += nowGold
            else:
                gold += count * nowWeight

            if nowSilver < count * nowWeight:
                silver += nowSilver
            else:
                silver += count * nowWeight

            if nowGold + nowSilver < count * nowWeight:
                total += nowGold + nowSilver
            else:
                total += count * nowWeight

        if gold >= a and silver >= b and total >= a+b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1


    return answer
