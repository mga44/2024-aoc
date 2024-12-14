import utils

"""
    1. list regions
    2. for each region iterate over each elem and check adjacent fields -> add to sum
    3. compute borders * number of elems
"""

grid = utils.read_2d_array("resources\\2024-12-12.txt")
max_x, max_y = utils.get_2d_array_size(grid)


grid_mask = list(list(0 for _ in range(max_x+1)) for _ in range(max_y+1))

def processed(index):
    return grid_mask[index[1]][index[0]] == 1


def in_border(x, y):
    return x >= 0 and y >= 0 and x <= max_x and y <= max_y


def process(index, plant, fence_area) -> tuple:  # (fence, area)
    if processed(index):
        return fence_area

    updated = (fence_area[0], fence_area[1] + 1)
    grid_mask[index[1]][index[0]] = 1
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dir in dirs:
        new_x = index[0] + dir[0]
        new_y = index[1] + dir[1]
        if in_border(new_x, new_y) and plant == grid[new_y][new_x]:
            updated = process((new_x, new_y), plant, updated)
        else:
            updated = (updated[0]+1, updated[1])


    return updated

areas = []
for i in range(max_y+1):
    for j in range(max_x+1):
        plant = grid[i][j]
        index = (j, i)
        if not processed(index):
            fence_area = process(index, plant, (0, 0))
            areas.append(fence_area)


print(areas)

print(grid_mask)


prices = list(map(lambda x: x[0]*x[1], areas))

print(f'All price sum is {sum(prices)}')