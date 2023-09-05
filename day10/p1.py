lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

register = 1
i = 0
cycle = 0
v = None

interest = [20, 60, 100, 140, 180, 220]
signals = {}

while i < len(lines):
    cycle += 1
    line = lines[i]

    if v is not None:
        i += 1
        register += v
        v = None
    else:
        tokens = line.split(" ")
        cmd = tokens[0]

        if cmd == "noop":
            i += 1
        elif cmd == "addx":
            v = int(tokens[1])

    signal = cycle * register
    print(f'"{line}"', cycle, register, signal)
    if cycle in interest:
        signals[cycle] = signal

print(signals)
print(sum(signals.values()))
