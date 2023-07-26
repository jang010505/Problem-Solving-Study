def solution(ingredient):
    answer = 0
    stack = list()

    for t in ingredient:
        stack.append(t)
        if len(stack) > 3 and stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
            answer += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()

    return answer