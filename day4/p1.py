lines = []
while True:
    try:
        lines.append(input())
    except:
        break


count = 0
for line in lines:
    left, right = line.split(",")
    ll, lr = [int(i) for i in left.split("-")]
    rl, rr = [int(i) for i in right.split("-")]

    if ll <= rl and rr <= lr:
        count += 1
    elif rl <= ll and lr <= rr:
        count += 1
    else:
        if rl <= ll:
            ll, lr, rl, rr = rl, rr, ll, lr
        if lr >= rl:
            count += 1
print(count)
