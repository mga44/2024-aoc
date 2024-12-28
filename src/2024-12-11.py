import utils

"""
    1. get line 
    2. for i in num_of blinks do operation
        3. change 0 -> 1
        4. if len(num) % 2 == 0 -> split into 2 stones 
        5. else num * 2024
    return num of stones
    
    
    0 -> mark as 1 (1)
    1 -> mark as to multiply (M) (1)
    M -> split into 20, 24 (2)
        -> 2 0 2 4 (4)
        -> 4048 1 4048 8096 (4)
        -> 40 48, 2024, 40 48, 80 96 (7)
        4 0 4 8, 20 24, 4 0 4 8, 8 0 9 6 
    
"""

def compute(input:int) -> list:
    if input == 0:
        return [1]
    
    num_size = len(str(input))
    if num_size % 2 == 0:
        half = int(num_size/2)
        first_stone = int(str(input)[:half])
        second_stone = int(str(input)[half:])
        return [first_stone, second_stone]
    
    return [input * 2024]

line = list(map(lambda x: int(x) ,utils.read_lines("resources\\2024-12-11.txt")[0].split(" ")))

stone_freq = dict((x,1) for x in line)
for i in range(75):
    tmp = {}
    for stone, f in stone_freq.items():
        new_stones = compute(stone)
        for s in new_stones:
            if s in tmp:
                tmp[s] += f
            else:
                tmp[s] = f
                
    stone_freq = tmp



print(f"Number of stones is {sum(stone_freq.values())}")