def solution(msg):

    dic = []
    for i in range(26):
        dic.append(chr(i+65))

    answer = []
    i = 0
    s = msg[0]

    while i != len(msg):
        if s in dic:
            if i != len(msg)-1:
                i += 1
            else:
                answer.append(dic.index(s)+1)
                break

            s += msg[i]
        else:
            dic.append(s)
            answer.append(dic.index(s[:-1])+1)
            s = msg[i]
    return answer