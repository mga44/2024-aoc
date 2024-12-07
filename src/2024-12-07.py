import utils

from functools import reduce
from operator import mul
"""
    1. read input
    2. for each line split result & "test data" list
    3. starting from the last index, div / subtract the latest number
    4. if sub is < 0 or div < 1 || not int - break 
    5. if conditions are met, take next (previous) val and do the same 
    6. if last variable is equal to remaining result - the params were valid -> add to list
    7. sum the elements in valid list
    * 
    8. create list of all possible combinations made from concatenation and evaluate it as well:
    9. for elem => combine with next one until it's greater than expected test result 
    10. run the same recurrent solution for every list until True 
"""

lines = utils.read_lines("resources\\2024-12-07.txt")


def parse_line(line:str):
    eq = line.split(':')
    result = int(eq[0])
    elements = [int(i) for i in eq[1].strip().split(" ")]
    return (result, elements)


# found solution: 132*1+8+714+972*5+21*1=9151
# return true if remaining result is eq to first elem, check - & / 
def test_eq(intermediate_result: float, elements, index_of_tested, operator, solution: str) -> bool:
    sum_el = sum(elements)
    mul_el = reduce(mul, elements)
    if sum_el == intermediate_result or mul_el == intermediate_result:
        return True
    
    # if sum_el > intermediate_result or mul_el < intermediate_result:
    #     return False
    
    if intermediate_result < 0 or not intermediate_result.is_integer():
        return False
    
    elem = elements[index_of_tested]
    if index_of_tested == 0:
        if intermediate_result == elem:
            solution=str(elem)+solution
            print(f'found solution: {solution}')
            return True;
        else:
            return False
            
    
    if operator == '-':
        solution = '+' + str(elem) + solution
        intermediate_result = intermediate_result - elem
    else: # div
        solution = '*' + str(elem) + solution
        intermediate_result = intermediate_result / elem
    
    index_of_tested -= 1
    return test_eq(intermediate_result, elements, index_of_tested, '-', solution) or test_eq(intermediate_result, elements, index_of_tested, '/', solution)


def test_equation(test_eq, result, elements):
    return test_eq(result, elements, len(elements)-1, '-', f'={result}') or test_eq(result, elements, len(elements)-1, '/', f'={result}')


def concat_list_elem(elements:list, result:int):
    # if sum of elems is greater than result, it's not gonna work
    #elements = elements.copy()
    if len(elements) == 1:
        if elements[0] == result:
            return True # return true
        else:
            return False # return false
    
    
    concatenated_lists = []
    for i in range(len(elements)-1): # last one doesn't need separate run
            
        e1 = elements[i]
        e2 = elements[i+1]
        concat_var = int(str(e1)+str(e2))
        if(concat_var > result):
            continue
    
        ne2 = elements.copy()
        ne2.pop(i+1)
        ne2.pop(i)
        ne2.insert(i, concat_var)
        # test concats here - if true return true
        if test_equation(test_eq, result, ne2):
            return True
        
        # concatenated_lists.append(ne2)
        if concat_list_elem(ne2, result):
            return True
    # for c in concatenated_lists:
        # if concat_list_elem(c, result):
            # return True
        
        
    return False
         
        


valid_test_results = []
equations = list(map(lambda x: parse_line(x), lines))


for eq in equations:
    result = eq[0]
    elements = eq[1]
    
    if test_equation(test_eq, result, elements):
        valid_test_results.append(result)
        continue
    
    #eval concat
    if concat_list_elem(elements, result):
        valid_test_results.append(result)
        continue
    

    
    print(f'No solution for {result}: {elements}')

print(f'Sum of valid test test results: {sum(valid_test_results)}') #10741443549536
# 10741443549536 - I'st part
# 16677162728270 too low