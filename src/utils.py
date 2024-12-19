from math import inf
import copy


def read_lines(filename:str) -> list:
    f = open(filename, "r")
    return f.readlines()

def read_2d_array(filename:str) -> list:
    return [list(s.replace("\n", "")) for s in read_lines(filename)]



def get_2d_array_size(arr):
    max_y = len(arr) - 1
    max_x = len(arr[0]) - 1
    return max_x, max_y

def print_2d_array(arr):
    s = ""
    for line in arr:
        for el in line:
            s+= str(el)
        s+="\n"
        
    print(s)

def find_char_in_2d_array(arr, character, single=True) -> tuple|list:
    result_list = []
    for i, line in enumerate(arr):
        for j, char in enumerate(line):
            if char == character:
                if single:
                    return (j, i)
                else:
                    result_list.append((j,i))
                    
    return result_list

def _get_neighbours(ind: tuple, node_dict: dict):
    neigbours = []
    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        potential_node = (ind[0] + dir[0], ind[1] + dir[1])
        if potential_node in node_dict:
            neigbours.append(potential_node)

    return neigbours

def dijkstra_pathfind(start: tuple, grid:list, obstacle_char='#') -> list:
    max_x, max_y = get_2d_array_size(grid)
    
    visited = copy.deepcopy(grid)
    visited[0][0] = 0
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