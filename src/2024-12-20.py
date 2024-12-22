import utils


grid = utils.read_2d_array('resources\\2024-12-20.txt')

start = utils.find_char_in_2d_array(grid, 'S')
end = utils.find_char_in_2d_array(grid, 'E')


def dijkstra_pathfind(start: tuple, grid:list, obstacle_char='#') -> list:
    max_x, max_y = get_2d_array_size(grid)
    
    visited = copy.deepcopy(grid)
    visited[start[1]][start[0]] = 0
    unvisited = {}
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            if grid[j][i] != obstacle_char:
                unvisited[(i, j)] = inf

    unvisited[start] = 0

    while unvisited != {}:
        min_unvisited_value = min(unvisited.values())
        unvisited_min_nodes = list(
            filter(lambda e: e[1] == min_unvisited_value, unvisited.items())
        )
        current_node = unvisited_min_nodes[0][0]
        near_nodes = _get_neighbours(current_node, unvisited)

        current_distance = visited[current_node[1]][current_node[0]]
        for next_node in near_nodes:
            new_distance = current_distance + 1
            old_dist = unvisited[next_node]
            if old_dist > new_distance:
                unvisited[next_node] = new_distance
                visited[next_node[1]][next_node[0]] = new_distance

        unvisited.pop(current_node)
        
    return visited

visited = dijkstra_pathfind(start, grid)

print(f'Initial distance to {end} is {visited[end[1]][end[0]]}')


"""
    go over path
"""
