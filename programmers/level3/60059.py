def spin(arr):
    return list(map(list, zip(*arr[::-1])))


def check(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i + N][j + N] != 1:
                return False

    return True


def solution(key, lock):
    N = len(lock)
    M = len(key)
    newLock = [[0] * 3 * N for i in range(3 * N)]

    for i in range(N):
        for j in range(N):
            newLock[i + N][j + N] = lock[i][j]

    for _ in range(4):
        key = spin(key)
        for li in range(2 * N):
            for lj in range(2 * N):
                for ki in range(M):
                    for kj in range(M):
                        newLock[li + ki][lj + kj] += key[ki][kj]

                if check(newLock, N):
                    return True

                for ki in range(M):
                    for kj in range(M):
                        newLock[li + ki][lj + kj] -= key[ki][kj]

    return False