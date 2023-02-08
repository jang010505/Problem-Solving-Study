def make_term_dict(terms):
    term_dict = dict()
    for term in terms:
        term_type, month = term.split()
        term_dict[term_type] = int(month)

    return term_dict

def make_day(day):
    y, m, d = map(int, day.split("."))
    return y*336 + m*28 + d

def check(privacy, today, term_dict):
    info_day, term_type = privacy.split()
    info_day = make_day(info_day)
    today = make_day(today)

    info_day += term_dict[term_type]*28 - 1

    if info_day >= today:
        return False
    else:
        return True


def solution(today, terms, privacies):
    answer = []
    term_dict = make_term_dict(terms)

    for i, privacy in enumerate(privacies):
        if check(privacy, today, term_dict):
            answer.append(i+1)

    return answer