def solution(new_id):

    # 1단계 소문자 치환
    new_id = new_id.lower()

    # 2단계 특정문자만 살리기
    id = new_id
    new_id = ""
    for char in id:
        if "a" <= char <= "z" or "0" <= char <= "9" or char == "-" or char == "_" or char == ".":
            new_id += char

    id = new_id
    new_id = id[0]
    for char in id[1:]:
        if new_id[-1] == "." and char == ".":
            continue
        else:
            new_id += char

    if len(new_id) > 0 and new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]

    if len(new_id) == 0:
        new_id += "a"

    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id[-1] == ".":
            new_id = new_id[:-1]

    while len(new_id) < 3:
        new_id += new_id[-1]

    answer = new_id
    return answer