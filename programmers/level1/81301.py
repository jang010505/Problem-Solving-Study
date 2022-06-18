def solution(s):
    wordToNumber = dict()
    wordDict = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
    wordToNumber["zero"] = "0"
    wordToNumber["one"] = "1"
    wordToNumber["two"] = "2"
    wordToNumber["three"] = "3"
    wordToNumber["four"] = "4"
    wordToNumber["five"] = "5"
    wordToNumber["six"] = "6"
    wordToNumber["seven"] = "7"
    wordToNumber["eight"] = "8"
    wordToNumber["nine"] = "9"

    answer = ""

    word = ""
    for char in s:
        if "0" <= char <= "9":
            answer += char
            continue
        word += char
        if word in wordDict:
            answer += wordToNumber[word]
            word = ""
    return int(answer)