import utils

lines = [i.strip() for i in utils.read_lines("resources\\2024-12-21.txt")]

"""
    translate char into position -> determine vector between p1 and p2.
    vector (num_1, num_2) == '>'*num_1 + '^'*num_2 (remember about the signs)
"""


numerical_keyboard = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["_", "0", "A"],
]

directional_keyboard = [
    ["_", "^", "A"],
    ["<", "v", ">"],
]


def vector(start: tuple, end: tuple) -> tuple:
    return (*(end[i] - start[i] for i in range(len(start))),)


def get_numeric_buttons(vector: tuple):
    horiz = ""
    vert = ""

    if vector[0] > 0:
        horiz = ">"
    elif vector[0] < 0:
        horiz = "<"

    if vector[1] > 0:
        vert = "v"
    elif vector[1] < 0:
        vert = "^"

    return horiz, vert


a_pos_numeric = (2, 3)
a_pos_directional = (2,0)

def get_instruction_directional(robot_numeric_instr: str) -> str:
    result_instruction = ""
    current_position_directional = a_pos_directional
    for char in robot_numeric_instr:
        char_pos = utils.find_char_in_2d_array(directional_keyboard, char)
        vector_directional_keyboard = vector(current_position_directional, char_pos)
        h, v = get_numeric_buttons(vector_directional_keyboard)
        # if current_position_numeric[1] == 0:
        # instr = v * abs(vector_directional_keyboard[1]) + h * abs(vector_directional_keyboard[0])  # moves from prev to char
        # else:
        instr = h * abs(vector_directional_keyboard[0]) + v * abs(vector_directional_keyboard[1])  # moves from prev to char
        current_position_directional = char_pos
        result_instruction += instr + "A"
    
    return result_instruction



results = []
for line in lines:
    current_position_numeric = a_pos_numeric
    current_position_directional = a_pos_directional
    robot_numeric_instr = ""
    human_instr = ""
    for char in line:
        char_pos = utils.find_char_in_2d_array(numerical_keyboard, char)
        vector_numeric_keyboard = vector(current_position_numeric, char_pos)
        h, v = get_numeric_buttons(vector_numeric_keyboard)
        if current_position_numeric[1] == len(numerical_keyboard)-1:
            instr = v * abs(vector_numeric_keyboard[1]) + h * abs(vector_numeric_keyboard[0])  # moves from prev to char
        else:
            instr = h * abs(vector_numeric_keyboard[0]) + v * abs(vector_numeric_keyboard[1])  # moves from prev to char
        current_position_numeric = char_pos

        robot_numeric_instr += instr + "A"

    print(f"Numeric robot instr: {robot_numeric_instr}")

    robot_1_directional_instr = get_instruction_directional(robot_numeric_instr)
    print(f"Directional robot 1 instr: {robot_1_directional_instr}")
    robot_2_directional_instr = get_instruction_directional(robot_1_directional_instr)
    print(f"Directional robot 2 instr: {robot_2_directional_instr}")
    results.append((line,robot_2_directional_instr))
    
    

print(f'Results: {results}')
results = [len(i[1])*int(i[0][:3]) for i in results]
print(f'Sum of complexities: {sum(results)}')



    
    
