def getStr(now, nxt):
    return ["".join(map(str, now))+"".join(map(str, nxt)), "".join(map(str, nxt))+"".join(map(str, now))]

def solution(dirs):
    answer = 0

    S = set()
    now = [0, 0]

    for c in dirs:
        now_x, now_y = now
        if c == "U":
            if now_x + 1 <= 5:
                nxt = [now_x+1, now_y]
                x, y = getStr(now, nxt)
                S.add(x)
                S.add(y)
                now = nxt
            else:
                continue
        elif c == "D":
            if now_x - 1 >= -5:
                nxt = [now_x-1, now_y]
                x, y = getStr(now, nxt)
                S.add(x)
                S.add(y)
                now = nxt
            else:
                continue
        elif c == "L":
            if now_y - 1 >= -5:
                nxt = [now_x, now_y-1]
                x, y = getStr(now, nxt)
                S.add(x)
                S.add(y)
                now = nxt
            else:
                continue
        elif c == "R":
            if now_y + 1 <= 5:
                nxt = [now_x, now_y+1]
                x, y = getStr(now, nxt)
                S.add(x)
                S.add(y)
                now = nxt
            else:
                continue


    return len(S)//2