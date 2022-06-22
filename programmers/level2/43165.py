answer = 0

def dfs(now, numbers, i, target):
    global answer
    if len(numbers) == i:
        if now == target:
            answer += 1
    else:
        dfs(now-numbers[i], numbers, i+1, target)
        dfs(now+numbers[i], numbers, i+1, target)


def solution(numbers, target):
    global answer
    dfs(0, numbers, 0, target)
    return answer