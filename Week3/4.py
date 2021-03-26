"""
4. Write a function that inverts the keys and values of a dictionary.
e.g. function_name({ 'a': 'b', 'c': 'd' }) => { 'b': 'a', 'd': 'c' }
e.g. function_name({ 'fruit': 'apple', 'meat': 'beef' }) => { 'apple': 'fruit', 'beef': 'meat' }
"""

def invert_dictionary(dictionary):
    inverted_dic = {}
    for i,j in dictionary.items():
        inverted_dic.update({j:i})

    print(inverted_dic)

invert_dictionary({ 'a': 'b', 'c': 'd' })
invert_dictionary({ 'fruit': 'apple', 'meat': 'beef' })
invert_dictionary({19:'Covid'})
