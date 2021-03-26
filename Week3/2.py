"""
2. Write function for list of elements (create own) that will return indices of all occurrences of that item in list
e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 'b') => [3, 4, 5]
e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 1) => [0, 6]
e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 'c') => []
"""


def indices_of_all_occurrences(input_list, element):
    result_list = []
    for i in input_list:
        if i == element:
            result_list.append(input_list.index(i))
    print(result_list)
    return result_list


indices_of_all_occurrences([1, 2, 4, 'b', 'b', 'b', 1], 'b')
indices_of_all_occurrences([1, 2, 4, 'b', 'b', 'b', 1], 1)
indices_of_all_occurrences([1, 2, 4, 'b', 'b', 'b', 1], 'c')
