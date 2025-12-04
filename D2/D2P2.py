data = open("input.txt", "r").read().split(",")
for i in range(len(data)):
    data[i] = data[i].split("-")

summation = 0
for idrange in data:
    for id in range(int(idrange[0]), int(idrange[1]) + 1):
        id = str(id)
        for i in range(len(id)//2):
            div, rem = divmod(len(id), i + 1)
            if rem == 0 and id[0 : i + 1] * div == id:
                summation += int(id) 
                break
print(summation)