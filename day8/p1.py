lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break


grid = list(map(lambda line: [int(i) for i in line], lines))
height, width = len(grid), len(grid[0])

visible = set()
for i in range(height):
    left = -1
    right = -1
    # Horizontal scan
    for j in range(width):
        lt = grid[i][j]
        rt = grid[i][width - j - 1]
        if lt > left:
            left = lt
            visible.add((i, j))
        if rt > right:
            right = rt
            visible.add((i, width - j - 1))

for j in range(width):
    # Vertical scan
    top = -1
    bottom = -1
    for i in range(height):
        ut = grid[i][j]
        bt = grid[height - i - 1][j]

        if ut > top:
            top = ut
            visible.add((i, j))
        if bt > bottom:
            bottom = bt
            visible.add((height - i - 1, j))

print(len(visible))
