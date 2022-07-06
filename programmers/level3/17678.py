def timeChange(timetable):
    lst = list()
    for time in timetable:
        h, m = time.split(":")
        lst.append(int(h) * 60 + int(m))
    return sorted(lst)


def change(time):
    return "{0:02d}:{1:02d}".format(time // 60, time % 60)


def solution(n, t, m, timetable):
    timetable = timeChange(timetable)

    lastTime = 540 + (n - 1) * t

    for time in range(540, lastTime + 1, t):
        if time == lastTime:
            count = 0
            while timetable and timetable[0] <= time:
                count += 1
                if count == m:
                    return change(timetable[0] - 1)
                timetable.pop(0)
            return change(time)
        else:
            count = 0
            while len(timetable) and timetable[0] <= time:
                count += 1
                timetable.pop(0)
                if count == m:
                    break