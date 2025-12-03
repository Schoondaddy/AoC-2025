data = open("input.txt", "r").read().split("\n")
## Tried: 6195, 6076
rotation = 50
count = 0
for move in data:
    dir = move[0]
    n = int(move[1:])
    
    if dir == "L":
        n *= -1
    
    if (rotation == 0) & (n < 0):
        count -= 1
    rotation += n
    if rotation >= 100:
        count += abs(rotation//100)
    elif rotation < 0:
        count += abs(rotation//100)
    elif rotation %100 == 0:
        count += 1
    rotation = rotation % 100
    

    
print(count)