def solution(n):
    answer = [0, 1]
    for i in range(1, n):
        answer.append((answer[-1] + answer[-2]) % 1234567)

    return answer[-1]