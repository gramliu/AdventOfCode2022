import sys

lines = []
while True:
    try:
        lines.append(input())
    except:
        break

# Rock Paper Scissors
c1 = ["A", "B", "C"]
c2 = ["X", "Y", "Z"]


def match(x, y):
    i1 = c1.index(x)
    i2 = c2.index(y) + 1
    state = (i2 - i1) % 3
    return state * 3 + i2


def match_state(x, state2):
    i1 = c1.index(x)
    state = c2.index(state2)
    offset = state - 1
    i2 = (i1 + offset) % 3 + 1
    return state * 3 + i2


score1 = 0
score2 = 0
for line in lines:
    x, y = line.split(" ")
    score2 += match(x, y)
    score1 += match_state(x, y)
print(score1)
print(score2)
