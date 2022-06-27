def solution(citations):
    answer = 0

    citations = sorted(citations, reverse=True)
    N = len(citations)

    for i in range(len(citations)):
        answer = max(answer, min(i+1, citations[i]))

    return answer