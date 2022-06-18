def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    student_answer = [0, 0, 0]

    for i in range(len(answers)):
        if student1[i%5] == answers[i]:
            student_answer[0] += 1
        if student2[i%8] == answers[i]:
            student_answer[1] += 1
        if student3[i%10] == answers[i]:
            student_answer[2] += 1

    max_answer = max(student_answer)
    answer = []

    for i in range(3):
        if student_answer[i] == max_answer:
            answer.append(i+1)

    return answer