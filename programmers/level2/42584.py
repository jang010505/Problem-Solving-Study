def solution(prices):
    answer = [0 for i in range(len(prices))]

    stack = list()

    for i in range(len(prices)):
        while stack and stack[-1][0] > prices[i]:
            price, now_i = stack.pop()
            answer[now_i] = i - now_i
        stack.append([prices[i], i])

    while stack:
        price, now_i = stack.pop()
        answer[now_i] = len(prices) - now_i - 1

    return answer