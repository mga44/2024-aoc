import utils
from math import inf
import copy

bytes = list(
    map(
        lambda ln: tuple(map(lambda c: int(c), ln.split(","))),
        utils.read_lines("resources\\2024-12-18.txt"),
    )
)

print(bytes)

max_x = 70
max_y = 70

grid = list(list("." for _ in range(max_x + 1)) for _ in range(max_y + 1))

utils.print_2d_array(grid)


bytes_fallen = 1024
for i in range(bytes_fallen):
    byte = bytes[i]

    grid[byte[1]][byte[0]] = "#"

visited = utils.dijkstra_pathfind((0,0), grid)

print(f"Distance to ({max_x},{max_y}) is {visited[max_y][max_x]}")
