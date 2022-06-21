def solution(num):
    answer = 0
    while num != 1:
        if answer >= 500:
            return -1

        if num % 2:
            num = 3 * num + 1
        else:
            num /= 2

        answer += 1
    return answer