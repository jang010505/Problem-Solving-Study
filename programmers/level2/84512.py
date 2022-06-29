def solution(word):
    answer = 0

    maxCount = 3905

    for i, char in enumerate(word):
        if char == 'A':
            answer += 1
        elif char == "E":
            answer += maxCount//pow(5, i+1)*1+1
        elif char == "I":
            answer += maxCount//pow(5, i+1)*2+1
        elif char == "O":
            answer += maxCount//pow(5, i+1)*3+1
        elif char == "U":
            answer += maxCount//pow(5, i+1)*4+1



    return answer