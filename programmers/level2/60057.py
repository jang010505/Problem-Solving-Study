def solution(s):
    answer = len(s)

    N = len(s)

    for num in range(1, len(s) // 2 + 1):
        i = 0
        newString = ""

        while i < N:
            pattern = s[i:i + num]
            count = 1
            i += num

            while i + num <= N and pattern == s[i:i + num]:
                count += 1
                i += num

            if count < 2:
                newString += pattern
            else:
                newString += str(count) + pattern

        answer = min(answer, len(newString))

    return answer