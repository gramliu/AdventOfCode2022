lines = []
while True:
    try:
        lines.append(input())
    except:
        break

crates = []
breakpoint = 0
for line in lines:
    breakpoint += 1
    if line == "":
        break

    tokens = line.split(" ")
    row = [None] * 9

    for i in range(9):
        if len(tokens) == 0:
            break
        if tokens[0] == "":
            tokens = tokens[4:]
        else:
            row[i] = tokens[0]
            tokens = tokens[1:]

    crates.append(row)

crates = crates[:-1]
crates = list(
    map(lambda row: list(map(lambda x: None if x is None else x[1:-1], row)), crates))

stacks = [[] for _ in range(9)]
for row in crates[::-1]:
    for i in range(9):
        if row[i] is not None:
            stacks[i].append(row[i])

for line in lines[breakpoint:]:
    instr = line.split(" ")
    count, src, dst = int(instr[1]), int(instr[3]) - 1, int(instr[5]) - 1
    src, dst = stacks[src], stacks[dst]

    changes = []
    for i in range(count):
        changes.append(src.pop())
    dst.extend(changes[::-1])

print([stack[-1] for stack in stacks])
