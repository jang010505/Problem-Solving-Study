def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    A = list()
    B = list()

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            A.append(str1[i] + str1[i + 1])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            B.append(str2[i] + str2[i + 1])

    if len(A) == 0 and len(B) == 0:
        return 65536

    a_temp = A.copy()
    a_result = A.copy()

    for c in B:
        if c not in a_temp:
            a_result.append(c)
        else:
            a_temp.remove(c)

    b_temp = A.copy()
    b_result = []

    for c in B:
        if c in b_temp:
            b_temp.remove(c)
            b_result.append(c)

    return (len(b_result) / len(a_result) * 65536) // 1