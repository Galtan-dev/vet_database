"""
script with general use functions
"""

def table_tuple_separation(name):
    """
    function for separating name from tuple, for example from tuple that i get
    in show tables mysql command
    """
    result = ''.join(filter(str.isalpha, name[0]))

    return result
