"""
1.  Write function for list of integers (create own) which returns list but with each element's index added to itself.
E.g function_name([0, 1, 3, 5]) => [0, 2, 5, 8]

"""


def add_index_to_itself(list_of_int):
    added_list_of_int = []
    for i in list_of_int:
        added_list_of_int.append(i+list_of_int.index(i))
    print(added_list_of_int)
    return added_list_of_int


add_index_to_itself([5, 9, 7, 12, 5684])
