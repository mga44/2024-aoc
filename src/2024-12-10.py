import utils
import copy
from collections import defaultdict
"""
    1. read input - create list with index of each '0'
    2. for each 0 (=i) -> until there's '9'
        3. check number in each dir - if it's i+1 go there, if no, go back
        4. when you get 9, return success 
        5. add index of '0' and number of successes to result list
    6. return list result
    
    
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

area_map = utils.read_2d_array('resources\\2024-12-10.txt')


starts = []
for i in range(len(area_map)):
    for j in range(len(area_map[i])):
        if area_map[i][j] == '0':
            starts.append((j,i))
            
        area_map[i][j] = int(area_map[i][j])


max_x, max_y = utils.get_2d_array_size(area_map)

def move_possible(current_level:int, current_index: tuple,  desired_direction:tuple) -> bool:
    new_y = current_index[1] + desired_direction[1]
    new_x = current_index[0] + desired_direction[0]
    if new_x < 0 or new_x > max_x or new_y <0 or new_y > max_y:
        return False
    
    adjacent_field = area_map[new_y][new_x]
    
    return adjacent_field == current_level + 1



counter = 0
trail_scores = defaultdict(set) # (('0' index), score)
def move(current_level:int, current_index:tuple, direction:tuple, grid, start) -> bool:
    if current_level == 9:
        trail_scores[start].add(current_index)
        global counter
        counter+=1
        print(f"found a way to {current_index}")
        return True
    
    if not move_possible(current_level, current_index, direction):
        return False
    
    new_y = current_index[1] + direction[1]
    new_x = current_index[0] + direction[0]
    next_index = area_map[new_y][new_x]
    
    grid[new_y][new_x] = '.'

    proceed(current_level+1, (new_x, new_y), grid, start)


def proceed(current_level:int, current_index:tuple, grid, start) ->bool:
    (
        move(current_level, current_index, (1,0), grid, start) or 
        move(current_level, current_index, (0,1), grid, start) or 
        move(current_level, current_index, (-1,0), grid, start) or 
        move(current_level, current_index, (0,-1), grid, start)
    )   

for start in starts:
    print(f'Starting at {start}')
    grid = copy.deepcopy(area_map)
    proceed(0, start, grid, start)
    
    
    l = ""
    for line in grid:
        for point in line: 
            l += str(point)
        l+= "\n"
        
    print(l)
    print("-------------------------")
       





score_sum = sum(list(map(lambda x: len(x), trail_scores.values())))


print(f"Sum of trail scores is {score_sum}")
print(f'Sum of ratings is {counter}')