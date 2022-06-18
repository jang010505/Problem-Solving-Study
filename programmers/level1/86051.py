def solution(numbers):
    numbers = set(numbers)
    array = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    answer = sum(array-numbers)
    return answer