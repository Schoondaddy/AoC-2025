data = open("input.txt", "r").read().split("\n")

for i in range(len(data)):
    data[i] = tuple(int(x) for x in data[i].split(","))

max_area = 0
while len(data) != 0:
    for i in range(1, len(data)):
        a = abs((data[0][0] - data[i][0] + 1) * (data[0][1] - data[i][1] + 1))
        if a > max_area:
            max_area = a
    data.pop(0)

print(max_area)