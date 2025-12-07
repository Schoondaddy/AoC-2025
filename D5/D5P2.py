data = open("input.txt", "r").read().split("\n\n")
ranges = data[0].split("\n")

for i in range(len(ranges)):
    ranges[i] = ranges[i].split("-")
    ranges[i][0], ranges[i][1] = int(ranges[i][0]), int(ranges[i][1])

ranges.sort(key = lambda x: x[0])

# Join ranges
index = 0
while index < len(ranges) - 1:
    if ranges[index][1] >= ranges[index + 1][0]:
        if ranges[index][1] < ranges[index + 1][1]:
            ranges[index][1] = ranges[index + 1][1]
        ranges.pop(index + 1)
    else:
        index += 1

count = 0
for r in ranges:
    count += r[1] - r[0] + 1
print(count)