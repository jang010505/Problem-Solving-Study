def solution(id_list, report, k):
    report_list = dict()

    for id in id_list:
        report_list[id] = set()

    for info in report:
        id, target_id = info.split()
        report_list[id].add(target_id)

    report_count = dict()

    for id in id_list:
        report_count[id] = 0

    for values in report_list.values():
        for value in values:
            report_count[value] += 1

    answer = [0]*len(id_list)

    for i, id in enumerate(id_list):
        for report_id in report_list[id]:
            if report_count[report_id] >= k:
                answer[i] += 1

    return answer