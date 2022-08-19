from collections import Counter

N = int(input())

lst = []

for i in range(N):
    lst.append(int(input()))


lst.sort()
print(round(sum(lst)/N))
print(lst[N//2])

c = Counter(lst).most_common()

if len(c) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])
print(lst[-1]-lst[0])
