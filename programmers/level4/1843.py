def solution(arr):
    x = 0
    y = 0
    value = 0
    for idx in range(len(arr) - 1, -1, -1):
        if arr[idx] == '+':
            continue
        elif arr[idx] == '-':
            tempMin = x
            tempMax = y
            x = min(-(value + tempMax), -value + tempMin)
            minus = int(arr[idx + 1])
            y = max(-(value + tempMin), -minus + (value - minus) + tempMax)
            value = 0
        elif int(arr[idx]) >= 0:
            value += int(arr[idx])
    y += value
    return y
