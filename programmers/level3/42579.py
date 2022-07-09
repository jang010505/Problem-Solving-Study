from collections import defaultdict


def solution(genres, plays):
    answer = []

    genre = defaultdict(int)
    for g, p in zip(genres, plays):
        genre[g] += p

    genre = sorted(genre.items(), key=lambda x: x[1], reverse=True)

    for l, cnt in genre:
        arr = []
        for idx, (g, p) in enumerate(zip(genres, plays)):
            if g == l:
                arr.append([p, idx])

        arr = sorted(arr, key=lambda x: (x[0], -x[1]), reverse=True)

        for i in range(min(len(arr), 2)):
            answer.append(arr[i][1])

    return answer
