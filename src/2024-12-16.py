import utils
from copy import deepcopy


"""
    1. get S & E
    2. while ind(char) != ind(E) OR only way is to turn 180
        3. list possible moves - forward and/or rotate if it makes sense
        4. for each in list move/rotate and move
        5. when E is reached add to possible results
        
"""

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dir = dirs[0]  # (1,0)

grid = utils.read_2d_array("resources\\2024-12-16.txt")

visited = deepcopy(grid)

start = utils.find_char_in_2d_array(grid, "S")
end = utils.find_char_in_2d_array(grid, "E")


def move_in_direction(player, move, score):
    score+=1
    visited[player[1]][player[0]] = 'X'
    x = move["ind"][0]
    y = move["ind"][1]
    return((x,y), score)


def rotate_and_move(player, move, score):
    score+=1000
    visited[player[1]][player[0]] = 'X'  
    x = move["ind"][0]
    y = move["ind"][1]
    return((x,y), score)

def perform(player, end, dir, score):
    possible_moves = []
    for d in dirs:
        next_x = player[0] + d[0]
        next_y = player[1] + d[1]
        if grid[next_y][next_x] == '#' or visited[next_y][next_x] == 'X':
            continue
        
        possible_moves.append({'ind':(next_x, next_y), "dir": d}) 
    
    # inverted_current = *(-i for i in dir),
    if len(possible_moves) < 1:
        print(f'Go back from {player}')
        return False
    
    pos_and_scores = []
    for move in possible_moves:
        if move['dir'] == dir:
            pos_and_score = move_in_direction(player, move, score)
        else:
            pos_and_score = rotate_and_move(player, move, score)
        
        print(f'Moving to {pos_and_score[0]}')            
        pos_and_scores.append(pos_and_score)
    
    
    for new_position in pos_and_scores: 
        if end == new_position[0]:
            print(f'Found solution with score {score}')
            return True
        
        perform(new_position[0], end, move['dir'], new_position[1])


player = start
print(f'Starting at {start}')
perform(player, end, dir, 0)