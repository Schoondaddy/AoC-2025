data = open("input.txt", "r").read().split("\n")

for i in range(len(data)):
    data[i] = list(data[i])

# pythonic transpose
data = [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]

summation = 0
i = 0
while i < len(data):
    op = data[i][4]
    num = 0
    if op == "*":
        num = 1
    for j in range(i, len(data)):
        if data[j] != [' ', ' ', ' ', ' ', ' ']:
            if op == "+":
                num += int("".join(data[j][:4]))
            else:
                num *= int("".join(data[j][:4]))
            if j != len(data) - 1:
                continue
        summation += num
        i = j + 1
        break

print(summation)