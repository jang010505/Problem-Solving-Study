def scoreDiffCompute(apeach_info, ryan_info):
    apeach_score = 0
    ryan_score = 0
    for i in range(11):
        if apeach_info[i] == ryan_info[i] == 0:
            continue
        elif apeach_info[i] < ryan_info[i]:
            ryan_score += 10 - i
        else:
            apeach_score += 10 - i

    return ryan_score - apeach_score


def f(count, apeach_info, ryan_info, remain_arrow):
    global answer, score
    if count == 11:
        if remain_arrow > 0:
            ryan_info[-1] += remain_arrow

        diff_score = scoreDiffCompute(apeach_info, ryan_info)
        if score < diff_score:
            score = diff_score
            answer = ryan_info.copy()

        ryan_info[-1] -= remain_arrow

    else:
        if apeach_info[10 - count] + 1 <= remain_arrow:
            ryan_info[10 - count] = apeach_info[10 - count] + 1
            f(count + 1, apeach_info, ryan_info, remain_arrow - apeach_info[10 - count] - 1)
            ryan_info[10 - count] = 0

        f(count + 1, apeach_info, ryan_info, remain_arrow)


def solution(n, info):
    global answer, score
    score = 0
    answer = [-1]
    ryan_info = [0] * 11
    f(0, info, ryan_info, n)
    return answer