def solution(s, n):
    answer = ""
    for i in range(len(s)):
        if s[i] == " ":
            answer += s[i]
        else:
            x = ord(s[i])
            if 65 <= x <= 90:
                x += n
                if 90 < x:
                    x -= 26
            else:
                x += n
                if 122 < x:
                    x -= 26
            answer += chr(x)
    return answer