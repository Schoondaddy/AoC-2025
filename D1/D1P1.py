input = open("input.txt", "r").read().split("\n")

rotation = 50
count = 0
for move in input:
    dir = move[0]
    n = int(move[1:])
    
    if dir == "L":
        n *= -1
    rotation = (rotation + n) % 100
    if rotation == 0:
        count += 1
    
print(count)