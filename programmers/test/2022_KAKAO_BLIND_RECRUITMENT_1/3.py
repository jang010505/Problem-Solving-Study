import math


def timeConvert(time):
    H, M = map(int, time.split(":"))
    return H * 60 + M


def feeCompute(fee_info, time):
    default_time, default_fee, unit_time, unit_fee = fee_info

    result = default_fee
    time -= default_time

    if time > 0:
        result += math.ceil(time / unit_time) * unit_fee

    return result


def solution(fees, records):
    car_info = dict()

    for record in records:
        time, number, info = record.split()

        now_time = timeConvert(time)

        if number in car_info:
            if car_info[number][1] == -1:
                car_info[number][1] = now_time
            else:
                pre_time = car_info[number][1]
                car_info[number][0] += now_time - pre_time
                car_info[number][1] = -1
        else:
            car_info[number] = [0, now_time, 0]

    for key in car_info:
        if car_info[key][1] != -1:
            car_info[key][0] += timeConvert("23:59") - car_info[key][1]
            car_info[key][1] = -1

        car_info[key][2] = feeCompute(fees, car_info[key][0])

    result = sorted(car_info.items(), key=lambda x: x[0])

    answer = []
    for number, info in result:
        answer.append(info[2])

    return answer