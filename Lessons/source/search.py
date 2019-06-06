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
            left_pointer = middle_index + 1
        else:
            right_pointer = middle_index - 1
    return None


def binary_search_recursive(array, item, left=0, right=None):
    if right is None:
        right = len(array) - 1

    middle_index = int(math.ceil((left + right) // 2))
    middle_value = array[middle_index]

    if middle_value == item:
        return middle_index
    elif middle_value < item:
        return binary_search_recursive(array, item, middle_index + 1, right)
    elif middle_value > item:
        return binary_search_recursive(array, item, left, middle_index - 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
numbers = [1,2,3,4,5]
result = binary_search_recursive(names, 'Nick')
print(result)
