def solution(n):
    answer = [0, 1, 2]
    for i in range(n):
        answer.append((answer[-2] + answer[-1]) % 1000000007)

    return answer[n]