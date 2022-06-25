def check(s):
    stack = list()

    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if char == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                stack.pop()
            elif char == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                stack.pop()
            elif char == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                stack.pop()

    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0

    for i in range(len(s)):
        s = s[1:] + s[0]
        if check(s):
            answer += 1

    return answer