def solution(numbers):
    answer = []
    answer = []
    for number in numbers:
        if number%4 == 3:
            temp = '0' + bin(number)[2:]
            for i in range(len(temp) - 1, -1, -1):
                if temp[i] == '0':
                    answer.append(int(temp[0:i] + "10" + temp[i + 2:], 2))
                    break
        else:
            answer.append(number+1)

    return answer