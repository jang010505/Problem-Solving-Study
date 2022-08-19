from itertools import permutations

def solution(n, weak, dist):
    answer = 0
    dist = sorted(dist, reverse=True)
    repair_lst = [()]

    for move in dist:
        repairs = []
        answer += 1

        for i, weakPoint in enumerate(weak):
            start = weakPoint
            ends = weak[i:] + [n + w for w in weak[:i]]

            print(ends)
            can = set()

            for end in ends:
                if end-start <= move:
                    can.add(end%n)

            repairs.append(can)
        can = set()

        for r in repairs:
            for x in repair_lst:
                new = r | set(x)
                if len(new) == len(weak):
                    return answer
                can.add(tuple(new))
        repair_lst = can

    return -1