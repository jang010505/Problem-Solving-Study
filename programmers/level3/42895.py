def solution(N, number):
    if number == N:
        return 1

    s = [set() for _ in range(8)]
    answer = 0

    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    for i in range(1, 9):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i+ 1
            break
    else:
        return -1
    return answer