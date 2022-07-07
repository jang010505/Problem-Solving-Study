def checkId(id1, id2):
    for i in range(len(id1)):
        if id2[i] == "*":
            continue
        elif id1[i] != id2[i]:
            return False

    return True

def f(now, user_id, banned_id, visit):
    global answer, answerSet
    if now == len(banned_id):
        s = "".join(map(str, visit))
        if s not in answerSet:
            answerSet.add(s)
            answer += 1
        return

    for i in range(len(user_id)):
        if visit[i] == 0 and len(user_id[i]) == len(banned_id[now]):
            if checkId(user_id[i], banned_id[now]):
                visit[i] = 1
                f(now + 1, user_id, banned_id, visit)
                visit[i] = 0


def solution(user_id, banned_id):
    global answer, answerSet
    answer = 0
    answerSet = set()

    visit = [0] * len(user_id)
    f(0, user_id, banned_id, visit)

    return answer