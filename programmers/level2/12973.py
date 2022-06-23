def solution(s):

    stack = list()

    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

    if len(stack):
        return 0
    else:
        return 1