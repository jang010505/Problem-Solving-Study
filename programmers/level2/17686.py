def slice(s):
    HEAD = ""
    NUMBER = ""
    TAIL = ""

    isNumber = False

    for i in range(len(s)):
        if s[i].isdigit():
            NUMBER += s[i]
            isNumber = True
        elif not isNumber:
            HEAD += s[i]
        else:
            TAIL = s[i:]
            break

    return [HEAD, NUMBER, TAIL]

def solution(files):
    answer = []

    for file in files:
        answer.append(slice(file))

    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))

    return ["".join(file) for file in answer]