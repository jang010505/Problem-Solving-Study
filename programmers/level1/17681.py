def solution(n, arr1, arr2):
    answer = [[" "] * n for i in range(n)]
    for i in range(len(arr1)):
        tmp = bin(arr1[i])[2:]
        for j in range(len(tmp)):
            if tmp[-j - 1] == "1":
                answer[i][-j - 1] = "#"

    for i in range(len(arr2)):
        tmp = bin(arr2[i])[2:]
        for j in range(len(tmp)):
            if tmp[-j - 1] == "1":
                answer[i][-j - 1] = "#"

        answer[i] = "".join(answer[i])

    return answer