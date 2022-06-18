def solution(N, stages):
    stage_info = [0 for i in range(N+1)]
    stage_try = [0 for i in range(N)]
    stages.sort()

    for x in stages:
        stage_info[x-1] += 1

    for i in range(N):
        stage_try[i] += sum(stage_info[i:])

    stage_fail = []

    for i in range(N):
        if stage_try[i] == 0:
            stage_fail.append(0)
        else:
            stage_fail.append(stage_info[i]/stage_try[i])

    result = sorted(stage_fail)

    answer = []

    for i in range(N-1,-1,-1):
        for j in range(N):
            if j+1 not in answer:
                if result[i] == stage_fail[j]:
                    answer.append(j+1)

    return answer