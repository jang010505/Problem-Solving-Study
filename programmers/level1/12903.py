def solution(s):
    right = 0
    if len(s)%2:
        left = len(s)//2
        right = len(s)//2+1
    else:
        left = len(s)//2-1
        right = len(s)//2+1
    return s[left:right]