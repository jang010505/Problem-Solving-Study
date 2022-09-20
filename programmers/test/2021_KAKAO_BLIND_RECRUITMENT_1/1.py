def stepOne(s):
    return s.lower()


def stepTwo(s):
    new_str = ""
    for x in s:
        if ('a' <= x <= 'z') or ("0" <= x <= "9") or x == "-" or x == "_" or x == ".":
            new_str += x

    return new_str


def stepThree(s):
    new_str = ""
    i = 0
    while i < len(s):
        if s[i] == ".":
            new_str += s[i]
            while i < len(s) and s[i] == ".":
                i += 1
        else:
            new_str += s[i]
            i += 1

    return new_str

def stepFour(s):
    new_str = s
    if new_str[0] == ".":
        new_str = new_str[1:]
    if 0 < len(new_str) and new_str[-1] == ".":
        new_str = new_str[:-1]
    return new_str

def stepFive(s):
    if s:
        return s
    else:
        return "a"

def stepSix(s):
    if len(s) < 15:
        return s
    elif s[14] == ".":
        return s[:14]
    else:
        return s[:15]

def stepSeven(s):
    new_str = s
    while len(new_str) < 3:
        new_str += new_str[-1]

    return new_str

def solution(new_id):
    return stepSeven(stepSix(stepFive(stepFour(stepThree(stepTwo(stepOne(new_id)))))))