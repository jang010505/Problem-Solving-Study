def solution(lottos, win_nums):
    win_nums = set(win_nums)

    win_count = 0
    zero_count = 0

    for number in lottos:
        if number == 0:
            zero_count += 1
        elif number in win_nums:
            win_count += 1

    answer = [7 - max(zero_count + win_count, 1), 7 - max(win_count, 1)]

    return answer