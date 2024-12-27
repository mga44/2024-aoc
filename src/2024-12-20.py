import utils


grid = utils.read_2d_array("resources\\2024-12-20.txt")

start = utils.find_char_in_2d_array(grid, "S")
end = utils.find_char_in_2d_array(grid, "E")

visited = utils.dijkstra_pathfind(start, grid)

distances = {}
pos = visited[end[1]][end[0]]
current_pos = end
while True:
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dir in dirs:
        next_pos = (*(dir[i] + current_pos[i] for i in range(len(current_pos))),)
        next_in_line = (*(dir[i] + next_pos[i] for i in range(len(next_pos))),)
        if not (
            utils.in_bounds(grid, next_pos) and utils.in_bounds(grid, next_in_line)
        ):
            continue

        if next_pos in distances:
            continue

        if (
            grid[next_pos[1]][next_pos[0]] == "#"
            and grid[next_in_line[1]][next_in_line[0]] in  ['.', 'S', 'E']
        ):
            grid[next_pos[1]][next_pos[0]] = "."
            new_visited = utils.dijkstra_pathfind(start, grid)
            new_distance = new_visited[end[1]][end[0]]["dist"]
            distances[next_pos] = new_distance
            grid[next_pos[1]][next_pos[0]] = "#"

    prev = pos["prev"]
    current_pos = prev
    if prev == ():
        break
    pos = visited[prev[1]][prev[0]]

result = {}
for d in distances.items():
    possible_gain = visited[end[1]][end[0]]["dist"] - d[1]
    if possible_gain in result:
        result[possible_gain] += 1
    else:
        result[possible_gain] = 1

r = sum(value for key, value in result.items() if key >= 100)
print(r) 

