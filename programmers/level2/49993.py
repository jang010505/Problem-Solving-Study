def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        S = ""
        for s in skills:
            if s in skill:
                S += s

        for i in range(len(skill) + 1):
            if S == skill[:i]:
                answer += 1
                break

    return answer