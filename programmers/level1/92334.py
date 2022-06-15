def solution(id_list, report, k):
    answer = []

    report_id = dict()
    report_count = dict()
    for name in id_list:
        report_id[name] = set()
        report_count[name] = 0

    for report_info in report:
        user_id, reported_id = report_info.split()
        if reported_id not in report_id[user_id]:
            report_id[user_id].add(reported_id)
            report_count[reported_id] += 1

    stop_id = set()
    for name in id_list:
        if reported_id[name] >= k:
            stop_id.add(name)

    for name in id_list:
        count = len(stop_id & report_id[name])
        answer.append(count)

    return answer