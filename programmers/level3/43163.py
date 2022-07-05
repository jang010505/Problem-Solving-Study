from collections import deque


def possible(word1, word2):
    count = 0
    for x, y in zip(word1, word2):
        if x != y:
            count += 1

    if count == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if target not in words:
        return 0

    dq = deque()
    dq.append([begin, 0])
    visit = [0] * len(words)
    answer = len(words)
    while dq:
        nowWord, cost = dq.popleft()
        if nowWord == target:
            answer = min(answer, cost)

        for i, nxtWord in enumerate(words):
            if possible(nowWord, nxtWord) and visit[i] == 0:
                visit[i] = 1
                dq.append([nxtWord, cost + 1])

    return answer