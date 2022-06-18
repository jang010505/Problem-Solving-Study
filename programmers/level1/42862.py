def solution(n, lost, reserve):
    array = [1 for i in range(n)]

    lost = set(lost)
    reserve = set(reserve)

    lost = lost -(lost & reserve)
    reserve = reserve - (lost & reserve)

    lost = list(lost)
    reserve = list(reserve)

    for stu in lost:
        array[stu - 1] = 0

    for stu in sorted(reserve):
        if stu != 1 and array[stu - 2] == 0:
            array[stu - 2] = 1
        elif stu < n:
            array[stu] = 1

    answer = sum(array)
    return answer