data = open("input.txt", "r").read().split("\n\n")
ranges = data[0].split("\n")
ids = data[1].split("\n")

for i in range(len(ranges)):
    ranges[i] = ranges[i].split("-")
    ranges[i][0], ranges[i][1] = int(ranges[i][0]), int(ranges[i][1])

ranges.sort(key = lambda x: x[0])

# Join ranges
index = 0
while index < len(ranges) - 1:
    if ranges[index][1] > ranges[index + 1][0]:
        if ranges[index][1] < ranges[index + 1][1]:
            ranges[index][1] = ranges[index + 1][1]
        ranges.pop(index + 1)
    else:
        index += 1

count = 0
for id in ids:
    id = int(id)
    print(id)
    for r in ranges:
        if id > r[0]:
            if id < r[1]:
                count += 1
                break
        else:
            break
print(count)