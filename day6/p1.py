lines = []
while True:
    try:
        lines.append(input())
    except:
        break

line = lines[0]
n = len(line)
ans = 0
for i in range(0, n - 4):
    marker = line[i:i+14]
    if len(set(marker)) == 14:
        ans = i + 14
        break
print(ans)
