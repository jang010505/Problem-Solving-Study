def change(s):
    newS = ""
    count = 0
    for c in s:
        if c == "0":
            count += 1
        else:
            newS += c

    return bin(len(newS))[2:], count


def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        s, count = change(s)
        answer[1] += count

    return answer