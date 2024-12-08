import utils
from collections import defaultdict
from math import sqrt, pow

"""
    1. parse input
    2. get computation data in form of {'anenna_freq': [(coord)]}
    3. for each 2 points in freq create new formula: y = ax + b -> distance: sqrt((x1-x2)^2+(y1-y2)^2) // 
        ..........
        ...#...... (3, 1)
        ..........
        ....a..... (4,4)
        ..........
        .....a.... (5,5)
        ..........
        ......#... (6, 7)
        ..........
        ..........
        
        0123456789
        aaX....... (0|1) -> x = 2, d(a1=x)=2, d(a2)=1
        a.a.X..... (0|2) -> x => x = 4 d(a1)=4, d(a2)=2
        aXXa...... (0|3) -> x => x = 1|2 d(a1)=4, d(a2)=2
        
        ________________________________________
        vector to go from one to other a2 + v1 = X1 (same in opposite direction) 
        0123456789
        aaX....... (0|1) -> v = (1), d(a1=x)=2, d(a2)=1
        a.a.X..... (0|2) -> v = (2)  d(a1)=4, d(a2)=2
        aXXa..X... (0|3) -> v = (3)  d(a1)=4, d(a2)=2 -> if |Vx| and |Vy| is divisible by 3, divide and perform the same operation for points between a1 & a2 
        
    4. get list of points that adhere to this formula (0 < x,y < x,y _max)
    5. for each point calculate distance from p1,p2 -> if one is 2x greater than other, add to set of antinodes
"""
grid = utils.read_2d_array("resources\\2024-12-08.txt")
max_x, max_y = utils.get_2d_array_size(grid)

antennas = defaultdict(list)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        possible_antenna = grid[i][j]
        if possible_antenna != ".":
            antennas[possible_antenna].append((j, i))


def produce_possible_antinodes(point, vect):  # vect is used to tranform p1 into p2
    result = []
    in_bounds = lambda p: not (
                    p[0] < 0
                    or p[0] > max_x
                    or p[1] < 0
                    or p[1] > max_y
                )
    
    new_p = point
    while in_bounds(new_p):
        new_p = (new_p[0] + vect[0], new_p[1] + vect[1])
        result.append(new_p)
        
    new_p2 = point
    while in_bounds(new_p2):
        new_p2 = (new_p2[0] - vect[0], new_p2[1] - vect[1])
        result.append(new_p2)
  
    return result


antinodes = set()
for antenna, points in antennas.items():
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            v = (p2[0] - p1[0], p2[1] - p1[1])
            # for p1, p2 add v/neg_v. check if pos p3 is
            
            ant_nodes = produce_possible_antinodes(p1, v)
            ant_nodes.extend(produce_possible_antinodes(p2, v))
            
            antinodes.add(p1)
            antinodes.add(p2)
            for pos_antinode in ant_nodes:

                if (
                    pos_antinode[0] < 0
                    or pos_antinode[0] > max_x
                    or pos_antinode[1] < 0
                    or pos_antinode[1] > max_y
                ):
                    continue

                antinodes.add(pos_antinode)


print(f"Number of unique antinodes: {len(antinodes)}")
