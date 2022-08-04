def solution(distance, rocks, n):
    answer = 0
    right, left = 0, distance

    rocks.sort()

    while right <= left:
        mid = (right + left) // 2
        delStones = 0
        preStone = 0
        for rock in rocks:
            if rock - preStone < mid:
                delStones += 1
            else:
                preStone = rock

            if delStones > n:
                break

        if delStones > n:
            left = mid - 1
        else:
            answer = mid
            right = mid + 1

    return answer