data = open("input.txt", "r").read().split("\n")

def clamp(value, minimum, maximum):
    return minimum if value < minimum else maximum if value > maximum else value

for i in range(len(data)):
    data[i] = list(data[i])

count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "@":
            area = data[clamp(i - 1, 0, len(data)) : clamp(i + 1, 0, len(data)) + 1]
            components = []
            for k in range(len(area)):
                components += area[k][clamp(j - 1, 0, len(data[i])) : clamp(j + 1, 0, len(data[i])) + 1]
            if components.count("@") < 5:
                count += 1
print(count)