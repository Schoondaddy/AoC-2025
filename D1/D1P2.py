data = open("input.txt", "r").read().split("\n")

rotation = 50
count = 0
for move in data:
    n = int(move[1:]) * (-1 if move[0] == "L" else 1)
    
    if (rotation == 0) & (n < 0):
        count -= 1
    
    rotation += n
    
    if rotation == 0:
        count += 1
    elif (rotation < 0) or (rotation >= 100):
        count += abs(rotation//100)
        if (rotation % 100 == 0) & (rotation < 0):
            count += 1
    
    rotation %= 100
    
print(count)