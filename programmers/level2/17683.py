def solution(m, musicinfos):

    def tokenizing(string):
        chars = {'C#': 'c',
                 'D#': 'd',
                 'F#': 'f',
                 'G#': 'g',
                 'A#': 'a',
                 'E#': 'e'}

        melody = []
        for i in range(len(string)-1):
            if string[i+1] == '#':
                melody.append(chars[string[i:i+2]])
            elif string[i] != '#':
                melody.append(string[i])
        if string[i+1] != '#':
            melody.append(string[i+1])
        return ''.join(melody)

    def convert(t):
        hour, minute = t.split(':')
        return (int(hour)*60)+int(minute)

    m = tokenizing(m)
    song = dict()
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start, end, melody = convert(start), convert(end), tokenizing(melody)
        elapsed, n = end-start, len(melody)
        melody = melody * (elapsed//n) + melody[:elapsed%n]
        song[title] = melody

    k = v = ''
    for key, value in song.items():
        if (m in value) and (len(v) < len(value)):
            k, v = key, value
    return '(None)' if len(k) == 0 else k