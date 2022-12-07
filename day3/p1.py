import sys

lines = []
while True:
    try:
        lines.append(input())
    except:
        break


def score(c: str):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


sum = 0
p = []
for line in lines:
    letters = line
    if len(p) < 3:
        p.append(set(letters))
    else:
        p1, p2, p3 = p
        inter = p1.intersection(p2).intersection(p3)
        for i in inter:
            sum += score(i)
        p = [set(letters)]

p1, p2, p3 = p
inter = p1.intersection(p2).intersection(p3)
for i in inter:
    print(i)
    sum += score(i)
p = []
print(sum)
