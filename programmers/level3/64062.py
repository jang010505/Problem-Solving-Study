def check(stones, mid, k):
    count = 0
    for s in stones:
        if s - mid < 0:
            count += 1
        else:
            count = 0

        if count == k:
            return False

    return True


def solution(stones, k):
    answer = 0

    left = min(stones)
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2

        if check(stones, mid, k):
            left = mid + 1
            answer = max(answer, mid)
        else:
            right = mid - 1
    return answer