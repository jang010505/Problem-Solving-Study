def solution(n, k, cmd):
    info = ["O"] * n
    now = k
    stack = []

    down = dict()
    up = dict()

    for i in range(n):
        down[i] = i + 1
        up[i] = i - 1

    down[-1] = 0
    up[n] = n - 1

    for txt in cmd:
        if txt[0] == "U":
            _, num = txt.split()
            num = int(num)
            for i in range(num):
                now = up[now]

        elif txt[0] == "D":
            _, num = txt.split()
            num = int(num)
            for i in range(num):
                now = down[now]


        elif txt[0] == "C":
            info[now] = "X"
            d = down.pop(now)
            u = up.pop(now)
            down[u] = d
            up[d] = u
            stack.append([u, now, d])
            if d == n:
                now = u
            else:
                now = d

        elif txt[0] == "Z":
            q = stack.pop()
            u, m, d = q[0], q[1], q[2]
            info[m] = "O"
            down[u] = m
            down[m] = d
            up[d] = m
            up[m] = u

    return "".join(info)
