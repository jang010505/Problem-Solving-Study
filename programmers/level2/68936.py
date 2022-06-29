def ispossible(x, y, size, info):
    char = info[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if char != info[i][j]:
                return False

    return True

def divide(x, y, size, info):
    if ispossible(x, y, size, info):
        if info[x][y] == 0:
            return [1, 0]
        else:
            return [0, 1]
    else:
        answer = [0, 0]
        a, b = divide(x, y, size//2, info)
        answer[0] += a
        answer[1] += b
        a, b = divide(x, y+size//2, size//2, info)
        answer[0] += a
        answer[1] += b
        a, b = divide(x+size//2, y, size//2, info)
        answer[0] += a
        answer[1] += b
        a, b = divide(x+size//2, y+size//2, size//2, info)
        answer[0] += a
        answer[1] += b
        return answer

def solution(arr):
    return divide(0, 0, len(arr), arr)