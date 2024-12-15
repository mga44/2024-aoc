import utils

"""
    1. read file, instructions
    2. for instruction
        3. if nothing -> move
        4. if wall -> stop
        5. if box ->
            6. check next (+x) cells in dir
            7. if empty -> swap box <-> empty
            8. if wall -> do nothing
            
    9. compute  gps coordinates -> print sum
"""


def get_input():
    lines = utils.read_lines("resources\\2024-12-15.txt")
    grid = []
    instructions = ""
    switch = False
    for line in lines:
        line = line.strip()
        if line == "":
            switch = True
            continue

        if switch:
            instructions += line
        else:
            grid.append(list(line))

    return grid, instructions


grid, instruction = get_input()

dirs = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


char_coordinates = ()
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "@":
            char_coordinates = (j, i)
            break

print(char_coordinates)
step = 0
for instr in instruction:
    dir = dirs[instr]
    next_field_y = char_coordinates[1] + dir[1]
    next_field_x = char_coordinates[0] + dir[0]
    next_field = grid[next_field_y][next_field_x]
    if next_field == "#":
        pass
    elif next_field == ".":
        grid[next_field_y][next_field_x] = "@"
        grid[char_coordinates[1]][char_coordinates[0]] = "."
        char_coordinates = (next_field_x, next_field_y)
    else: # box 'O' on the way
        check_x_field = 2
        dir_inc = *(i*check_x_field for i in dir),
        new_y = char_coordinates[1] + dir_inc[1]
        new_x = char_coordinates[0] + dir_inc[0]
        field_after_obstacle = grid[new_y][new_x]
        while field_after_obstacle == 'O':
            check_x_field+=1
            dir_inc = *(i*check_x_field for i in dir),
            new_y = char_coordinates[1] + dir_inc[1]
            new_x = char_coordinates[0] + dir_inc[0]
            field_after_obstacle = grid[new_y][new_x]
        
        if field_after_obstacle == '#':
            pass
        else:
            #swap 'next_field' (O) with 'field_after_obstacle' (.)
            #swap character (@) with 'next_field' (.)
            #translates to 
            # ind(character) = '.'
            # ind(next_field) = '@'
            # ind(field_after_obstacle) = '0'
            
            grid[char_coordinates[1]][char_coordinates[0]] = "."
            grid[next_field_y][next_field_x] = "@"
            grid[new_y][new_x] = "O"
            char_coordinates = (next_field_x, next_field_y)
    
    step += 1
    print(f'Step: {step}, direction {instr}')
    
            
gps_coordinates = []
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "O":
            gps_coordinates.append(i*100 + j)

print(f"Sum of GPS coordinates is {sum(gps_coordinates)}")
