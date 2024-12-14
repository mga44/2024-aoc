import utils

"""
    1. list regions
    2. for each region iterate over each elem and check adjacent fields -> add to sum
    3. compute borders * number of elems
"""

grid = utils.read_2d_array("resources\\2024-12-12.txt")
max_x, max_y = utils.get_2d_array_size(grid)


grid_mask = list(list(0 for _ in range(max_x + 1)) for _ in range(max_y + 1))

fence_mask = list(list([] for _ in range(max_x + 1)) for _ in range(max_y + 1))


def processed(index):
    return grid_mask[index[1]][index[0]] == 1


def in_border(x, y):
    return x >= 0 and y >= 0 and x <= max_x and y <= max_y


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
    grid_mask[index[1]][index[0]] = 1
    print_log(plant, f"Processing {index}")
    next = []
    for dir in dirs:
        new_x = index[0] + dir[0]
        new_y = index[1] + dir[1]

        if in_border(new_x, new_y) and plant == grid[new_y][new_x]:
            # updated = process((new_x, new_y), plant, updated)
            next.append((new_x, new_y))
        else:
            fence_mask[index[1]][index[0]].append(dir)
            increment = True
            for x in dir_translator.get(dir):
                other_index = (index[0] + x[0], index[1] + x[1])
                if in_border(other_index[0], other_index[1]):
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


# for i in range(max_y + 1):
#     for j in range(max_x + 1):
#         plant = grid[i][j]
#         for dir in dirs:
#             new_y = i + dir[1]
#             new_x = j+dir[0]
#             if not in_border(new_x, new_y):
#                 fence_mask[i][j].append(dir)
#                 continue

#             other_plant = grid[new_y][new_x]
#             if  plant != other_plant:
#                 fence_mask[i][j].append(dir)


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
