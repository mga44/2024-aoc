import copy
import utils

"""
    1. read lines 
    2. note starting index and orientation
    3. while starting is not repeated
    4. check if can move in appropriate orientation 
    5. YES -> move in orientation & mark previous field as X
    6. NO -> change orientation 
    7. do until guard lefts the map
    8. count X's + guard char
    *
    9. after we ensure that the guard can move try to place the obstacle in the following index
    10. each time perform all computations until:
        a. guard leaves the map 
        b. guard position is repeated (increment counter)
    do this until guard exits
    
"""

grid = utils.read_2d_array("resources\\2024-12-06.txt")

ORIENTATION_VECTORS = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}  # vectors are in (x,y) format; think of grid[y][x]
ORIENTATION_ROTATE_ORDER = ("^", ">", "v", "<")

max_x, max_y = utils.get_2d_array_size(grid)


def can_move(orientation: str, index: tuple, grid=grid):
    move_vector = ORIENTATION_VECTORS[orientation]
    x = index[0] + move_vector[0]
    y = index[1] + move_vector[1]
    will_leave_the_area = x < 0 or y < 0 or x > max_x or y > max_y
    if will_leave_the_area:
        return (-1, -1)
    if grid[y][x] != "#":
        return (x, y)
    else:
        return ()


def get_initial_position():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in ORIENTATION_VECTORS.keys():
                return (j, i), grid[i][j]


initial_index, initial_orientation = get_initial_position()
current_index, current_orientation = initial_index, initial_orientation


def check_infinite_loop(grid, current_orientation, current_index) -> bool:
    visited = {(current_orientation, current_index)}
    copy_grid = copy.deepcopy(grid)
    pos_to_place_obstacle = can_move(
        current_orientation, current_index, grid=copy_grid
    )  # we already know that can move
    # if pos_to_place_obstacle is 'X' then it was visited and cannot be changed!
    if copy_grid[pos_to_place_obstacle[1]][pos_to_place_obstacle[0]] == "X":
        return False

    copy_grid[pos_to_place_obstacle[1]][pos_to_place_obstacle[0]] = "#"

    while True:
        next_position = can_move(current_orientation, current_index, grid=copy_grid)
        if next_position == (-1, -1):  # leaves the map
            return False
        if next_position:  # move
            copy_grid[current_index[1]][current_index[0]] = "X"
            copy_grid[next_position[1]][next_position[0]] = current_orientation
            current_index = next_position
        else:  # rotate
            ind = ORIENTATION_ROTATE_ORDER.index(current_orientation)
            if ind == len(ORIENTATION_ROTATE_ORDER) - 1:
                ind = 0
            else:
                ind += 1
            current_orientation = ORIENTATION_ROTATE_ORDER[ind]

        if (current_orientation, current_index) in visited:
            return True

        visited.add((current_orientation, current_index))


infinite_loops = 0
#note: should've revorked this as very similar code is called in check_infinite_loop
while True:
    next_position = can_move(current_orientation, current_index)
    if next_position == (-1, -1):  # leaves the map
        break
    if next_position:  # move
        if check_infinite_loop(grid, current_orientation, current_index):
            infinite_loops += 1

        grid[current_index[1]][current_index[0]] = "X"
        grid[next_position[1]][next_position[0]] = current_orientation
        current_index = next_position
    else:  # rotate
        ind = ORIENTATION_ROTATE_ORDER.index(current_orientation)
        if ind == len(ORIENTATION_ROTATE_ORDER) - 1:
            ind = 0
        else:
            ind += 1
        current_orientation = ORIENTATION_ROTATE_ORDER[ind]

visited_counter = 1
for i in grid:
    for j in i:
        if j == "X":
            visited_counter += 1

print(f"Number of visited cells: {visited_counter}")
print(f"Number of infinite loops detected: {infinite_loops}")
