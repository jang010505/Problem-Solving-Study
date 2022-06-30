def solution(s):
    answer = True
    stack = list()

    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) and stack[-1] == "(":
                stack.pop()
            else:
                answer = False

    if len(stack):
        answer = False

    return answer