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
    
    num_size = len(str(num))
    if num_size % 2 == 0:
        half = int(num_size/2)
        first_stone = int(str(input)[:half])
        second_stone = int(str(input)[half:])
        return [first_stone, second_stone]
    
    return [num * 2024]


line = list(map(lambda x: int(x) ,utils.read_lines("resources\\2024-12-11.txt")[0].split(" ")))

zero_cache = []
easy_result_cache = {0:[1]}
for i in range(75):
    if i == 0:
        zero_cache.append([0])
        continue
    
    i_result = []
    for num in zero_cache[i-1]:
        if num in easy_result_cache:
            r = easy_result_cache[num]
            i_result.extend(r)
        else:
            r = compute(num)
            i_result.extend(r)
            easy_result_cache[num] = r
        
    zero_cache.append(i_result)
    
    


zeroes = []
result = line
for i in range(75):
    new_result = []
    for num in result:
        if isinstance(num, tuple):
            zeroes.append(num)
            continue
        
        if num in easy_result_cache:
            new_result.extend(easy_result_cache[num])
            continue
        
        num_size = len(str(num))
        if num == 0:
            new_result.append((0, i))
        elif num_size % 2 == 0:
            half = int(num_size/2)
            first_stone = int(str(num)[:half])
            second_stone = int(str(num)[half:])
            new_result.append(first_stone)
            new_result.append(second_stone)
        else:
            new_result.append(num * 2024)
    result = new_result



print(f"Number of stones is {len(result)}")