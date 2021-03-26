"""
3. Create a function that takes an integer and returns its length.
e.g. function_name(8) => 1
e.g. function_name(88) => 2
e.g. function_name(83894) => 5
(Can't use len)
"""

def length_of_int(integer):
    result = 0
    str_out_of_integer = str(integer)
    for i in str_out_of_integer:
        result += 1
    print(result)
    return result

length_of_int(8)
length_of_int(88)
length_of_int(83894)