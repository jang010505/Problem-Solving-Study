def findLastZero(s):
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            return i
    return -1


def solution(s):
    answer = []

    for txt in s:
        count = 0
        S = ""
        for i in range(len(txt)):
            S += txt[i]
            if S[-3:] == "110":
                count += 1
                S = S[:-3]

        idx = findLastZero(S)
        if idx == -1:
            answer.append(count*"110"+S)
        else:
            answer.append(S[:idx+1] + count*"110" + S[idx+1:])

    return answer