def solution(k, room_number):
    room_dic = {}
    ret = []

    for number in room_number:
        n = number
        visit = [n]

        while n in room_dic:
            n = room_dic[n]
            visit.append(n)

        ret.append(n)

        for now in visit:
            room_dic[now] = n+1

    return ret