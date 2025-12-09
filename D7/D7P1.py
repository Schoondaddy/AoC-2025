data = open("input.txt", "r").read().split("\n")

indices = [data[0].find("S")]
splits = 0
for layer in data:
    new_indices = []
    layer = list(layer)
    for index in indices:
        if layer[index] == "^":
            layer[index] = "X"
            splits += 1
            if index + 1 < len(layer):
                new_indices.append(index + 1) 
                layer[index + 1] = "|"
            if index - 1 >= 0:
                new_indices.append(index - 1)
                layer[index - 1] = "|"
        else:
            new_indices.append(index)
            layer[index] = "|"
    
    indices = list(dict.fromkeys(new_indices))
    print(layer)
    


print(splits)