def getDay(s):
    return map(int, s.split("."))

def computeValidity(today, day, validity_term):
    now_Y, now_M, now_D = getDay(today)
    target_Y, target_M, target_D = getDay(day)

    target_M += validity_term
    while target_M > 12:
        target_M -= 12
        target_Y += 1

    target_D -= 1
    if target_D < 1:
        target_D += 28
        target_M -= 1
        if target_M < 1:
            target_M += 12
            target_Y -= 1

    if target_Y < now_Y:
        return False
    elif target_Y > now_Y:
        return True
    else:
        if target_M < now_M:
            return False
        elif target_M > now_M:
            return True
        else:
            if target_D < now_D:
                return False
            elif target_D >= now_D:
                return True

def solution(today, terms, privacies):

    validity = dict()

    for term in terms:
        t, m = term.split()
        validity[t] = int(m)

    answer = []
    for i, privacy in enumerate(privacies):
        day, validity_type = privacy.split()
        if not computeValidity(today, day, validity[validity_type]):
            answer.append(i+1)

    return answer