import utils
from collections import defaultdict

lines = utils.read_lines('resources\\2024-12-23.txt')

groups = defaultdict(list)
for line in lines:
    g = line.strip().split('-')
    if g[0] in groups:
        groups[g[0]].append(g[1])
    else:
        groups[g[0]] = [g[1]]
        
    if g[1] in groups:
        groups[g[1]].append(g[0])
    else:
        groups[g[1]] = [g[0]]
        
print(groups)

connections = set()
for k, v in groups.items():
    for val in v:
        for val2 in groups[val]:
            if val2 in v:
                result = [k, val, val2]
                if not any(x.startswith('t') for x in result):
                    continue
                result.sort()
                result = ",".join(result)
                connections.add(result)

print(connections)

connections = set(filter(lambda x: 't' in x, connections))
print('\n'.join(connections))
print(len(connections))

