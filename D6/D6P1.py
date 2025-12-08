data = open("input.txt", "r").read().split("\n")

for i in range(len(data)):
    data[i] = data[i].split()

summation = 0
for j in range(len(data[0])):
    product = 1
    for i in range(len(data) - 1):
        if data[len(data) - 1][j] == "+":
            summation += int(data[i][j])
        else:
            product *= int(data[i][j])
    if data[len(data) - 1][j] == "*":
        summation += product
print(summation)