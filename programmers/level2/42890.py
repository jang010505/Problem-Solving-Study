from itertools import combinations

def solution(relation):
    N = len(relation)
    M = len(relation[0])

    lst = []
    for i in range(M):
        lst.extend(combinations(range(M), i+1))

    answer = 0

    unique = []
    for array in lst:
        tmp = [tuple([item[key] for key in array]) for item in relation]

        if len(set(tmp)) == N:
            check = True

            for x in unique:
                if set(x).issubset(set(array)):
                    check = False
                    break

            if check:
                unique.append(array)

    return len(unique)