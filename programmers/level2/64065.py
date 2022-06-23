def solution(s):
    lst = list()
    temp = list()
    s = s[1:-1].split(',')

    for x in s:
        if x[0] == "{":
            temp = list()
            if x[-1] == "}":
                temp.append(int(x[1:-1]))
                lst.append(temp)
            else:
                temp.append(int(x[1:]))
        elif x[-1] == "}":
            temp.append(int(x[:-1]))
            lst.append(temp)
        else:
            temp.append(int(x))

    lst = sorted(lst, key=lambda x:len(x))

    answer = []

    for l in lst:
        y = set(l)
        x = set(answer)
        answer.append(list(y-x)[0])


    return answer
