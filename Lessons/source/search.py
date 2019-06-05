import math


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index
    return None


def linear_search_recursive(array, item, index=0):
    if index > len(array) - 1:
        return None
    elif array[index] is item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)
    return None


def binary_search_iterative(array, item):
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer <= right_pointer:
        middle_index = int(math.ceil(left_pointer + right_pointer) / 2)
        middle_value = array[middle_index]

        if middle_value == item:
            return middle_index
        elif middle_value < item:
            left_pointer += 1
        else:
            right_pointer -= 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    left_pointer = 0
    right_pointer = len(array) - 1

    middle_index = int(math.ceil(left_pointer + right_pointer) / 2)
    middle_value = array[middle_index]

    if middle_value == item:
        return middle_index
    elif middle_value < item:
        return binary_search_recursive(array, item, left=left_pointer + 1)
    else:
        return binary_search_recursive(array, item, right=right_pointer - 1)

    return None


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


names = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']
result = linear_search_recursive(names, "Julia")
print(result)
