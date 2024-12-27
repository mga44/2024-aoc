from math import inf
import heapq


def read_lines(filename:str) -> list:
    f = open(filename, "r")
    return [i.strip() for i in f.readlines()]

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

def _get_neighbours(ind: tuple, grid: list, obstacle_char='#'):
    max_x, max_y = get_2d_array_size(grid)
    x,y = ind
    return  [
            (x + dx, y + dy)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if 0 <= x + dx <= max_x and 0 <= y + dy <= max_y
            and grid[y + dy][x + dx] != obstacle_char
        ]

def dijkstra_pathfind(start: tuple, grid: list, obstacle_char="#") -> list:
    max_x, max_y = get_2d_array_size(grid)
    visited = [
        [{"dist": inf, "prev": ()} for _ in range(max_x + 1)] for _ in range(max_y + 1)
    ]
    visited[start[1]][start[0]]["dist"] = 0
    unvisited = [(0, start)]
    while unvisited:
        current_distance, current_node = heapq.heappop(unvisited)
        near_nodes = _get_neighbours(current_node, grid, obstacle_char)

        for next_node in near_nodes:
            new_distance = current_distance + 1
            old_dist = visited[next_node[1]][next_node[0]]["dist"]
            if old_dist > new_distance:
                visited[next_node[1]][next_node[0]]["dist"] = new_distance
                visited[next_node[1]][next_node[0]]["prev"] = current_node
                heapq.heappush(unvisited, (new_distance, (next_node[0], next_node[1])))

    return visited



def in_bounds(array:list, index:tuple) -> bool:
    max_x, max_y = get_2d_array_size(array) 
    return not (
                    index[0] < 0
                    or index[0] > max_x
                    or index[1] < 0
                    or index[1] > max_y
                )