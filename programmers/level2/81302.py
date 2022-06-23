def solution(places):
    answer = []
    for place in places:
        info = []
        check = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    info.append([i, j])

        for now_i, now_j in info:
            for nxt_i, nxt_j in info:
                distance = abs(now_i-nxt_i)+abs(now_j-nxt_j)
                if distance == 0:
                    continue
                elif distance == 1:
                    check = 0
                elif distance == 2:
                    if now_i == nxt_i:
                        if now_j < nxt_j:
                            if place[now_i][now_j+1] != "X":
                                check = 0
                        else:
                            if place[now_i][now_j-1] != "X":
                                check = 0
                    elif now_j == nxt_j:
                        if now_i < nxt_i:
                            if place[now_i+1][now_j] != "X":
                                check = 0
                        else:
                            if place[now_i-1][now_j] != "X":
                                check = 0
                    else:
                        if now_i < nxt_i:
                            if now_j < nxt_j:
                                if not (place[now_i+1][now_j] == "X" and place[now_i][now_j+1] == "X"):
                                    check = 0
                            else:
                                if not (place[now_i+1][now_j] == "X" and place[now_i][now_j-1] == "X"):
                                    check = 0
                        else:
                            if now_j < nxt_j:
                                if not (place[now_i-1][now_j] == "X" and place[now_i][now_j+1] == "X"):
                                    check = 0
                            else:
                                if not (place[now_i-1][now_j] == "X" and place[now_i][now_j-1] == "X"):
                                    check = 0
        if check:
            answer.append(1)
        else:
            answer.append(0)
    return answer