def solution(jobs):
    answer = 0
    nowTime = 0
    jobs = sorted(jobs, key=lambda x: x[1])
    count = 0
    N = len(jobs)
    visit = [0 for i in range(N)]
    answer = 0
    while count < N:
        nxt = -1
        for i, x in enumerate(jobs):
            if x[0] <= nowTime and visit[i] == 0:
                nxt = i
                visit[i] = 1
                break
        else:
            nowTime += 1
            continue

        count += 1
        nowTime += jobs[nxt][1]
        answer += nowTime - jobs[nxt][0]

    return answer // N