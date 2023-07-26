def compute(users, emoticons, info):
    result = [0, 0]

    for i in range(len(users)):
        discount, m = users[i]
        fee = 0
        for j, dis in enumerate(info):
            if discount <= dis:
                fee += emoticons[j] * ((100 - dis) / 100)
        if fee >= m:
            result[0] += 1
        else:
            result[1] += fee

    return result


def dfs(users, emoticons, n, info, count):
    global answer
    if count == n:
        result = compute(users, emoticons, info)

        if result[0] > answer[0]:
            answer = result
        elif result[0] == answer[0] and result[1] > answer[1]:
            answer = result
        return

    for i in [10, 20, 30, 40]:
        info[count] = i
        dfs(users, emoticons, n, info, count + 1)
        info[count] = 0


def solution(users, emoticons):
    global answer
    answer = [0, 0]
    dfs(users, emoticons, len(emoticons), [0] * len(emoticons), 0)
    return answer