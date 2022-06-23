from itertools import permutations


def solution(expression):
    answer = 0
    operator = ['+', '-', '*']
    priorities = list(map(list, permutations(operator)))

    for priority in priorities:
        new = []
        first = expression.split(priority[0])
        for section in first:
            second = section.split(priority[1])
            second = [str(eval(x)) for x in second]
            new.append(priority[1].join(second))

        new = [str(eval(x)) for x in new]
        result = abs(eval(priority[0].join(new)))

        if result > answer:
            answer = result

    return answer