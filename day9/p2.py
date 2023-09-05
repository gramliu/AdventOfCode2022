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


def dist(p1, p2):
    """
    Return the Chebyshev distance between the two points
    """
    x1, y1 = p1
    x2, y2 = p2

    return max(abs(x1 - x2), abs(y1 - y2))


def print_visited(visited):
    lo_x, hi_x = -11, 14
    lo_y, hi_y = -5, 15
    for i in range(hi_y, lo_y - 1, -1):
        for j in range(lo_x, hi_x + 1):
            if (j, i) == (0, 0):
                print("s", end="")
            elif (j, i) in visited:
                print("#", end="")
            else:
                print(".", end="")
        print()


def print_rope(pos):
    lo_x, hi_x = -11, 14
    lo_y, hi_y = -5, 15
    mapping = {}
    for i in range(len(pos)):
        mapping[pos[i]] = i
    for i in range(hi_y, lo_y - 1, -1):
        for j in range(lo_x, hi_x + 1):
            if (j, i) == (0, 0):
                print("s", end="")
            elif (j, i) in mapping:
                idx = mapping[(j, i)]
                if idx == 0:
                    print("H", end="")
                else:
                    print(idx, end="")
            else:
                print(".", end="")
        print()
    print("===")


visited = set()
visited.add((0, 0))

pos = [(0, 0) for _ in range(10)]
for line in lines:
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
    pos[0] = pos[0][0] + dx, pos[0][1] + dy

    for i in range(1, len(pos)):
        hx, hy = pos[i - 1]
        tx, ty = pos[i]

        sign_x = sign(hx - tx)
        sign_y = sign(hy - ty)

        while dist((tx, ty), (hx, hy)) > 1:
            dx = abs(tx - hx)
            dy = abs(ty - hy)
            if dx > 1:
                tx += sign_x
                if dy >= 1:
                    ty += sign_y
            elif dy > 1:
                ty += sign_y
                if dx == 1:
                    tx += sign_x
            if i == 9:
                #print(tx, ty)
                visited.add((tx, ty))
        pos[i] = tx, ty

    # print(pos)
    print_rope(pos)

print(len(visited))
# #print(visited)
# print(lo_x, hi_x)
# print(lo_y, hi_y)
print_visited(visited)
