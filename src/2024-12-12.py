import utils

"""
    1. list regions
    2. for each region iterate over each elem and check adjacent fields -> add to sum
    3. compute borders * number of elems
"""

grid = utils.read_2d_array("resources\\2024-12-12.txt")
max_x, max_y = utils.get_2d_array_size(grid)


processed_mask = list(list(0 for _ in range(max_x + 1)) for _ in range(max_y + 1))
fence_mask = list(list([] for _ in range(max_x + 1)) for _ in range(max_y + 1))

def processed(index: tuple):
    x,y = index
    return processed_mask[y][x] == 1

dir_translator = {
    (-1, 0): [(0, 1), (0, -1)],
    (1, 0): [(0, 1), (0, -1)],
    (0, 1): [(1, 0), (-1, 0)],
    (0, -1): [(1, 0), (-1, 0)],
}


def print_log(plant, msg):
    if plant == "F":
        print(msg)


dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def process(index, plant, fence_area) -> tuple:  # (fence, area)
    if processed(index):
        return fence_area

    updated = (fence_area[0], fence_area[1] + 1)
    processed_mask[index[1]][index[0]] = 1
    print_log(plant, f"Processing {index}")
    for dir in dirs:
        new_x = index[0] + dir[0]
        new_y = index[1] + dir[1]

        if utils.in_bounds(grid, (new_x, new_y)) and plant == grid[new_y][new_x]:
            next.append((new_x, new_y))
        else:
            fence_mask[index[1]][index[0]].append(dir)
            increment = True
            for x in dir_translator.get(dir):
                other_index = (index[0] + x[0], index[1] + x[1])
                if utils.in_bounds(grid, other_index):
                    other_plant = grid[other_index[1]][other_index[0]]
                    other_fence = fence_mask[other_index[1]][other_index[0]]
                    if plant == other_plant and dir in other_fence:
                        print_log(
                            plant,
                            f"*{index} Has fence on {other_index} in direction {dir}",
                        )
                        increment = False

            fence_count = updated[0]
            if increment:
                print_log(plant, f"**Adding fence for {index} in direction {dir}")
                fence_count += 1

            updated = (fence_count, updated[1])

    for e in next:
        updated = process((e[0], e[1]), plant, updated)

    return updated

part_1 = False
if part_1:
    areas = []
    for i in range(max_y + 1):
        for j in range(max_x + 1):
            plant = grid[i][j]
            index = (j, i)
            if not processed(index):
                fence_area = process(index, plant, (0, 0))
                areas.append(fence_area)


    print(areas)

    prices = list(map(lambda x: x[0] * x[1], areas))

    print(f"All price sum is {sum(prices)}")


# part 2
# --------------------------------------------------------------

processed_mask = list(list(0 for _ in range(max_x + 1)) for _ in range(max_y + 1))
fence_mask = list(list([] for _ in range(max_x + 1)) for _ in range(max_y + 1))

def get_region(initial_index: tuple, plant: str) -> set:
    
    fields_in_regions = set()
    if processed(initial_index):
        return fields_in_regions
    
    fields_in_regions.add(initial_index)
    next = []
    processed_mask[initial_index[1]][initial_index[0]] = 1
    for dir in dirs:
        candidate = tuple(initial_index[i] + dir[i] for i in range(len(dir)))
        if utils.in_bounds(grid, candidate) and grid[candidate[1]][candidate[0]] == plant:
            if not processed(candidate):
                next.append(candidate)
        else:
            fence_mask[initial_index[1]][initial_index[0]].append(dir)
            
    for n in next:
        r = get_region(n, plant)
        fields_in_regions.update(r)
        
    return fields_in_regions


regions = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        index = (j,i)
        plant = grid[i][j]
        if not processed(index):
            region = get_region(index, plant)
            regions.append({'plant': plant, 'region':region})

corners = {
    (-1,-1): [(-1,0), (0,-1)],
    (1,-1): [(1,0), (0,-1)],
    (-1,1): [(-1,0), (0,1)],
    (1,1): [(1,0), (0,1)],
}

for r in regions:
    plant = r['plant']
    region_only = r['region']
    corner_count = 0
    for field in region_only:
        for corner, checks in corners.items():
            c1 = tuple(field[i] + checks[0][i] for i in range(len(field)))
            c2 = tuple(field[i] + checks[1][i] for i in range(len(field)))
            
            p1, p2 = '', ''
            if utils.in_bounds(grid, c1):
                p1 = grid[c1[1]][c1[0]]
            if utils.in_bounds(grid, c2):
                p2 = grid[c2[1]][c2[0]]
        
            d =  tuple(field[i] + corner[i] for i in range(len(field)))
            diagonal = 'diagonal'
            if utils.in_bounds(grid, d):
                diagonal = grid[d[1]][d[0]]
            if (diagonal == p1 or diagonal == p2) and diagonal == plant:
                continue
            
            check_1 = plant == p1
            check_2 = plant == p2
            if check_1 == check_2:
                corner_count +=1
            
    r['corners'] = corner_count

res = [len(r['region']) * r['corners'] for r in regions]

print(f'Bulk price is {sum(res)}')