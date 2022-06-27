from collections import deque

def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    answer = 0
    while people:
        if len(people) > 1 and  people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        else:
            people.popleft()
        answer += 1
    return answer