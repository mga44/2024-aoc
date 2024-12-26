import utils

lines = utils.read_lines("resources\\2024-12-25.txt")

keys = []
locks = []
tmp = []
for k, line in enumerate(lines):
    if line != "":
        tmp.append(line)
    
    if line == '' or k == len(lines)-1:
        if tmp[0] == "#####":
            lock = [0 for _ in tmp[0]]
            for i, lvl in enumerate(tmp):
                for j, pos in enumerate(lvl):
                    if pos == "#":
                        lock[j] = i
            locks.append(lock)
        else:
            tmp.reverse()
            key = [0 for _ in tmp[0]]
            for i, lvl in enumerate(tmp):
                for j, pos in enumerate(lvl):
                    if pos == "#":
                        key[j] = i
            keys.append(key)
        tmp = []

print(locks)
print(keys)

fittings = set()
for l, lock in enumerate(locks):
    for k, key in enumerate(keys):
        result = [lock[i] + key[i] for i in range(len(key))]
        if all([f <=5 for f in result]):
            fittings.add((l,k))


print(len(fittings))