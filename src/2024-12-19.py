import utils

lines = utils.read_lines("resources\\2024-12-19.txt")

towels = list(i.strip() for i in lines[0].split(','))
towels.sort(key=lambda el: len(el), reverse=True)
patterns = [i.strip() for i in lines[2:]]

towel_sizes = set((len(i) for i in towels))
not_found_patterns = []

def check_pattern(towels, pattern: str) -> bool:
    if pattern == '':
        return True
    
    if pattern in not_found_patterns:
        return False
    
    for towel in towels:
        if pattern.startswith(towel):
            new_pattern = pattern.removeprefix(towel)
            if check_pattern(towels, new_pattern):
                return True
    
    not_found_patterns.append(pattern)
    return False


possible_designs = []
cnt= 0
for pattern in patterns:
    cnt+=1
    print(f'Processing {cnt} / {len(patterns)}')
    if check_pattern(towels, pattern):
        possible_designs.append(pattern)

print(f'Number of valid designs is {len(possible_designs)}')
print(possible_designs)