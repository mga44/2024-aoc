import utils

# pairs opcode (operation), operand (number)


lines = utils.read_lines('resources\\2024-12-17.txt')



A = int(lines[0].replace("Register A: ", ''))
B = int(lines[1].replace("Register B: ", ''))
C = int(lines[2].replace("Register C: ", ''))

instructions = list(int(i) for i in lines[4].replace('Program: ', '').split(','))




def get_combo_value(num: int) -> int:
    match num:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case 7:
            return

        case _:
            return



pointer = 0
out = []
while pointer < len(instructions):
    opcode = instructions[pointer]
    number = instructions[pointer+1]
    move_pointer = True
    match opcode:
        case 0:
             A = int(A / 2 ** get_combo_value(number)) # write to A
        case 1:
            B = B ^ number #write to B
        case 2:
            B = get_combo_value(number) % 8 #write to B
        case 3:
            if A != 0:
                pointer = number
                move_pointer = False
        case 4:
            B = B ^ C
        case 5:
            out.append(get_combo_value(number)%8)
        case 6:
            B = int(A / 2 ** get_combo_value(number)) # write to A
        case 7:
            C = int(A / 2 ** get_combo_value(number)) # write to A

        case _:
            pass  
        
    if move_pointer:
        pointer+=2




print(f"out is {','.join(str(i) for i in out)}")
