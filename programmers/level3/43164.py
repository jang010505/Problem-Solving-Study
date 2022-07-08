def f(visit, now, tickets):
    global answer, x, check
    if sum(visit) == len(visit) and check:
        answer = x.copy()
        check = False
        return

    for i in range(len(tickets)):
        if now == tickets[i][0]:
            nxt = tickets[i][1]
            if visit[i] == 0:
                visit[i] = 1
                x.append(nxt)
                f(visit, nxt, tickets)
                x.pop()
                visit[i] = 0


def solution(tickets):
    global answer, x, check
    check = True
    x = ["ICN"]
    answer = []

    tickets = sorted(tickets, key=lambda x: (x[0], x[1]))

    visit = [0]*len(tickets)

    f(visit, "ICN", tickets)

    return answer