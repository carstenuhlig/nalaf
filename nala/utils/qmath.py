import math


"""
These are some quick math functions. NOTE: not requiring an external package like SciPy,
which does have those functions implemented.
"""

# todo implement test functions
def mean(arr_of_nr):
    """
    :param arr_of_nr: array of real numbers
    :return: average of array
    """
    if len(arr_of_nr) == 0:
        raise IndexError('no element in array')
    if not any(isinstance(x, (int, float)) for x in arr_of_nr):
        raise TypeError
    return sum(arr_of_nr)/len(arr_of_nr)

def hmean(arr_of_pos_nr):
    """
    harmonic mean
    :param arr_of_pos_nr: array of pos real numbers
    :return: harmonic mean
    """
    if len(arr_of_pos_nr) == 0:
        raise IndexError('no element in array')
    if not any(isinstance(x, (int, float)) and x >= 0 for x in arr_of_pos_nr):
        raise TypeError
    return len(arr_of_pos_nr) / sum(1/x for x in arr_of_pos_nr)
