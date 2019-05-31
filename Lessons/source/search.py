#!python
import math


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


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

    while left_pointer <= right_pointer:
        middle_index = 

    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


binary_search_iterative([1, 2, 2, 4, 1, 2, 3, 4,  5], 1)
