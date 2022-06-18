def solution(sizes):
    max_x = 0
    max_y = 0

    for x, y in sizes:
        if x < y:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        else:
            max_x = max(max_x, y)
            max_y = max(max_y, x)

    return max_y*max_x