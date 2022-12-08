from functools import reduce

lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

grid = list(map(lambda line: [int(i) for i in line], lines))

scores = {}
height, width = len(grid), len(grid[0])
for i in range(height):
    for j in range(width):
        left = right = up = down = 0
        t = grid[i][j]
        row_score = [0, 0, 0, 0]
        delta = [-1, 1]
        for k in range(4):
            row = k // 2
            col = k % 2
            dx = 0 if row == 0 else delta[col]
            dy = 0 if row == 1 else delta[col]

            y, x = i, j
            while x > 0 and x < width - 1 and y > 0 and y < height - 1:
                x += dx
                y += dy
                row_score[k] += 1
                if grid[y][x] >= t:
                    break

        score = reduce(lambda a, b: a * b, row_score)
        scores[(i, j)] = score


scores[(i, j)] = left * right * up * down
print(max(scores.values()))
