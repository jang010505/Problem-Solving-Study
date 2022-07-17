def solution(s):
    answer = 1

    N = len(s)

    for i in range(1, N):
        x = min(N - i - 1, i)
        check = x
        for j in range(x):
            if s[i + j + 1] != s[i - j - 1]:
                check = j
                break

        answer = max(answer, 1 + 2 * check)

    for i in range(1, N):
        if i <= N // 2:
            x = i
            check = x
            for j in range(x):
                if s[i + j] != s[i - j - 1]:
                    check = j
                    break
        else:
            x = N - i - 1
            check = x + 1
            for j in range(x):
                if s[i + j] != s[i - j - 1]:
                    check = j
                    break

        answer = max(answer, 2 * check)

    return answer