lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

for line in lines:
    cal = int(line)
    # Perform computation
