import sys

lines = sys.stdin.readlines()[0].split("\n")

best = 0
current = 0
cals = []
for line in lines:
    if len(line) == 0:
        cals.append(current)
        current = 0
    else:
        current += int(line)

cals.append(current)
cals.sort()
print(sum(cals[-3:]))
