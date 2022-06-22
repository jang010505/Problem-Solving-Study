def solution(record):
    answer = []
    lst = []
    userIdToNmae = dict()
    for text in record:
        if "Leave" in text:
            movement, userId = text.split()
        else:
            movement, userId, name = text.split()

        if movement == "Enter":
            userIdToNmae[userId] = name
            lst.append([userId, "님이 들어왔습니다."])
        elif movement == "Leave":
            lst.append([userId, "님이 나갔습니다."])
        elif movement == "Change":
            userIdToNmae[userId] = name

    for userId, text in lst:
        answer.append(userIdToNmae[userId] + text)

    return answer