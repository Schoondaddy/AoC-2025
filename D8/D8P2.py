import math

def dist(p1, p2):
    return sum([(p1[x] - p2[x])**2 for x in range(3)])


data = open("input.txt", "r").read().split("\n")
for i in range(len(data)):
    data[i] = data[i].split(",")
    data[i] = tuple([int(x) for x in data[i]])

groups = {x : [data[x]] for x in range(len(data))}

dists = {}
while len(data) != 0:
    for i in range(1, len(data)):
        d = dist(data[0], data[i])
        dists[d] = (data[0], data[i])
    data.pop(0)

dists = dict(sorted(dists.items()))
last_connection = None
for points in list(dists.values()):
    for group in list(groups.items()):
        if points[0] in group[1]:
            for group2 in groups.items():
                if points[1] in group2[1]:
                    if group == group2:
                        break
                    groups[group2[0]] += groups.pop(group[0])
                    if len(group2[1]) == 1000:
                        last_connection = points
                    break
            break
    if last_connection != None:
        break

print(last_connection[0][0] * last_connection[1][0])