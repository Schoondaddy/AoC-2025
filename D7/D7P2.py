data = open("input.txt", "r").read().split("\n")

indices = {
    data[0].find("S") : 1
    }
for layer in data:
    new_indices = {}
    layer = list(layer)
    for index in indices.keys():
        if layer[index] == "^":
            layer[index] = "X"
            if index + 1 < len(layer):
                if index + 1 not in new_indices.keys():
                    new_indices[index + 1] = indices[index]
                else:
                    new_indices[index + 1] += indices[index]
                layer[index + 1] = "|"
            if index - 1 >= 0:
                if index - 1 not in new_indices.keys():
                    new_indices[index - 1] = indices[index]
                else:
                    new_indices[index - 1] += indices[index]
                layer[index - 1] = "|"
        else:
            if index not in new_indices.keys():
                    new_indices[index] = indices[index]
            else:
                new_indices[index] += indices[index]
            layer[index] = "|"
    indices = new_indices
    
print(sum(indices.values()))