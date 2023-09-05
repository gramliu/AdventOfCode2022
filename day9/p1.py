lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break


def sign(x):
    if x < 0:
        return -1
    else:
        return 1


visited = set()
visited.add((0, 0))

tx, ty = 0, 0
hx, hy = 0, 0
for line in lines:
    # print(line)
    direction, amt = line.split(" ")
    amt = int(amt)

    mapping = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }

    delta = mapping[direction]
    dx, dy = delta[0] * amt, delta[1] * amt
    hx, hy = hx + dx, hy + dy

    #print(f"(hx, hy) = {(hx, hy)}")
    #print(f"(tx, ty) = {(tx, ty)}")

    if abs(hx - tx) > 1 or abs(hy - ty) > 1:
        # print("Adjusting")
        # need to adjust
        if abs(hx - tx) > 1 and hy == ty:
            # horizontal
            targetX = tx + (abs(hx - tx) - 1) * sign(hx - tx)
            while tx != targetX:
                tx += sign(hx - tx)
                #print(tx, ty)
                visited.add((tx, ty))
        elif abs(hy - ty) > 1 and hx == tx:
            # vertical
            targetY = ty + (abs(hy - ty) - 1) * sign(hy - ty)
            while ty != targetY:
                ty += sign(hy - ty)
                #print(tx, ty)
                visited.add((tx, ty))
        else:
            # diagonal
            targetX = tx + (abs(hx - tx) - 1) * sign(hx - tx)
            targetY = ty + (abs(hy - ty) - 1) * sign(hy - ty)
            #print(f"(targetX, targetY), {(targetX, targetY)}")
            if abs(hx - tx) == 1:
                targetX += sign(hx - tx)
            else:
                targetY += sign(hy - ty)
            while tx != targetX or ty != targetY:
                if tx != targetX:
                    tx += sign(hx - tx)
                if ty != targetY:
                    ty += sign(hy - ty)
                #print(tx, ty)
                visited.add((tx, ty))

print(len(visited))
