def solution(cap, n, deliveries, pickups):
    answer = 0
    box = [0, 0]

    count = 0
    d_lst = []
    i = n - 1

    while i >= 0:
        if count == 0 and deliveries[i]:
            d_lst.append(i)
            count += deliveries[i]
            while count > cap:
                count -= cap
                d_lst.append(i)
        elif count and deliveries[i]:
            count += deliveries[i]
            while count > cap:
                count -= cap
                d_lst.append(i)
        i -= 1

    count = 0
    p_lst = []
    i = n - 1

    while i >= 0:
        if count == 0 and pickups[i]:
            p_lst.append(i)
            count += pickups[i]
            while count > cap:
                count -= cap
                p_lst.append(i)
        elif count and pickups[i]:
            count += pickups[i]
            while count > cap:
                count -= cap
                p_lst.append(i)
        i -= 1

    p_lst = list(reversed(p_lst))
    d_lst = list(reversed(d_lst))

    if len(p_lst) > len(d_lst):
        while p_lst:
            if d_lst:
                if p_lst[-1] >= d_lst[-1]:
                    answer += (p_lst[-1] + 1) * 2
                else:
                    answer += (d_lst[-1] + 1) * 2

                p_lst.pop()
                d_lst.pop()
            else:
                answer += (p_lst[-1] + 1) * 2
                p_lst.pop()
    else:
        while d_lst:
            if p_lst:
                if p_lst[-1] >= d_lst[-1]:
                    answer += (p_lst[-1] + 1) * 2
                else:
                    answer += (d_lst[-1] + 1) * 2

                p_lst.pop()
                d_lst.pop()
            else:
                answer += (d_lst[-1] + 1) * 2
                d_lst.pop()

    return answer