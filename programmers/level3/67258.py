from collections import defaultdict


def solution(gems):
    answer = [1, len(gems)]
    gemTypeCount = len(set(gems))
    N = len(gems)
    result = N
    right = 0
    gemDict = defaultdict(int)

    for left, gem in enumerate(gems):
        while len(gemDict) < gemTypeCount and right < N:
            gemDict[gems[right]] += 1
            right += 1

        if len(gemDict) == gemTypeCount:
            if result > right - left:
                answer = [left + 1, right]
                result = right - left

        gemDict[gem] -= 1

        if gemDict[gem] == 0:
            del (gemDict[gem])

    return answer