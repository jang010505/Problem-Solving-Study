def solution(s):
    answer = ''
    data = s.split(" ")
    l = len(data)
    print(data)
    for i in range(l):
        if data[i] == '':
            answer += " "
            continue
        if data[i] != '':
            if data[i][0].isdigit():
                a = data[i].lower()
                answer += a

            if data[i][0].isalpha():
                b = data[i][0].upper()
                c = data[i][1:].lower()
                answer+=(b+c)

        answer += " "

    #print(answer)
    return answer[:-1]