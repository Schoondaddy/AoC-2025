import math
import copy

def dist(p1, p2):
    return math.sqrt(sum([(p1[x] - p2[x])**2 for x in range(3)]))


data = open("input.txt", "r").read().split("\n")
for i in range(len(data)):
    data[i] = data[i].split(",")
    data[i] = tuple([int(x) for x in data[i]])

groups = {data[x] : x for x in range(len(data))}

dists = {}
buffer = copy.deepcopy(data)
while len(buffer) != 0:
    for i in range(1, len(buffer)):
        d = dist(buffer[0], buffer[i])
        dists[d] = (buffer[0], buffer[i])
    buffer.pop(0)

dists = dict(sorted(dists.items()))

for points in list(dists.values())[:11]:
    groups[points[1]] = groups[points[0]]
print(groups)


group_count = [0 for i in range(len(groups))]
for i in groups.values():
    group_count[i] += 1
print(group_count)
group_count.sort(reverse= True)

print(group_count[0] * group_count[1] * group_count[2])