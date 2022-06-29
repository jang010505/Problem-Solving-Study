def solution(n):
    answer = [0, 3, 11]
    for i in range(2, n // 2):
        answer.append((4 * answer[-1] - answer[-2]) % 1000000007)

    return answer[n // 2]