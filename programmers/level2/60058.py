import sys

sys.setrecursionlimit(10 ** 6)


def check(s):
    stack = list()
    for char in s:
        if len(stack) == 0:
            if char == ")":
                return False
            else:
                stack.append(char)
        else:
            if char == ")":
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
    if len(stack) == 0:
        return True
    else:
        return False


def makeString(u, v):
    result = "("
    result += simulation(v)
    result += ")"
    for char in u[1:-1]:
        if char == "(":
            result += ")"
        else:
            result += "("
    return result


def simulation(s):
    if len(s) == 0:
        return ""

    answer = ""
    u = ""
    v = ""
    left = 0
    right = 0

    for i, char in enumerate(s):
        u += char
        if char == ")":
            right += 1
        else:
            left += 1

        if left == right:
            v = s[i + 1:]
            break

    if check(u):
        answer += u
        answer += simulation(v)
    else:
        answer += makeString(u, v)

    return answer


def solution(p):
    return simulation(p)