data = open("input.txt", "r").read().split(",")
for i in range(len(data)):
    data[i] = data[i].split("-")

summation = 0
for idrange in data:
    for id in range(int(idrange[0]), int(idrange[1]) + 1):
        id = str(id)
        if (len(id) % 2 == 0) & (id[0:len(id)//2] == id[len(id)//2:]):
            summation += int(id)
print(summation)