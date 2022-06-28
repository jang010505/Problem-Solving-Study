def solution(n, words):
    cycle = 1
    S = set()
    S.add(words[0])

    for i in range(1, len(words)):
        if i % n == 0:
            cycle += 1
        if words[i - 1][-1] != words[i][0]:
            return [(i) % n + 1, cycle]
        if words[i] in S:
            return [(i) % n + 1, cycle]
        if len(words[i]) == 1:
            return [(i) % n + 1, cycle]

        S.add(words[i])
    return [0, 0]