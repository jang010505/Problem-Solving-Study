def bs(lst, target):
    l = 0
    r = len(lst)
    while l < r:
        m = (l+r)//2

        if lst[m] < target:
            l = m+1
        else:
            r = m
    return len(lst) - r

def solution(info, query):
    language_info = {"cpp" : 0, "java" : 1, "python" : 2, "-" : 3}
    type_info = {"backend" : 0, "frontend" : 1, "-" : 2}
    career_info = {"junior" : 0, "senior" : 1, "-" : 2}
    food_info = {"chicken" : 0, "pizza" : 1, "-" : 2}

    lst = [[[[[] for l in range(3)] for k in range(3)] for j in range(3)] for i in range(4)]

    for s in info:
        language, type, career, food, score = s.split()
        for l in [language, "-"]:
            for t in [type, "-"]:
                for c in [career, "-"]:
                    for f in [food, "-"]:
                        lst[language_info[l]][type_info[t]][career_info[c]][food_info[f]].append(int(score))

    for i in range(4):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    lst[i][j][k][l].sort()

    answer = []

    for q in query:
        language, _, type, _, career, _, food, score = q.split()
        score = int(score)
        answer.append(bs(lst[language_info[language]][type_info[type]][career_info[career]][food_info[food]], score))


    return answer