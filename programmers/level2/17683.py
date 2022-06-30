def getTime(start, end):
    startH, startM = map(int, start.split(":"))
    endH, endM = map(int, end.split(":"))
    return (endH * 60 + endM) - (startH * 60 + startM)


def solution(m, musicinfos):
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")

    lst = list()

    for i, musicinfo in enumerate(musicinfos):
        startTime, endTime, name, melody = musicinfo.split(",")
        time = getTime(startTime, endTime)

        melody = melody.replace("C#", "c")
        melody = melody.replace("D#", "d")
        melody = melody.replace("F#", "f")
        melody = melody.replace("G#", "g")
        melody = melody.replace("A#", "a")

        melody = melody * time
        melody = melody[:time]
        if m in melody:
            lst.append([time, name, i])

    lst = sorted(lst, key=lambda x: (-x[0], x[2]))

    if len(lst):
        return lst[0][1]
    else:
        return "(None)"