def solution(s):
    lst = s.split(" ")
    result = list()
    for x in lst:
        answer = ""
        for i in range(len(x)):
            if i % 2 == 0:
                answer += x[i].upper()
            else:
                answer += x[i].lower()
        result.append(answer)

    return ' '.join(result)