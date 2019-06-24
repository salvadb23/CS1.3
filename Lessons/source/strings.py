#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Average case O(n ** 2) - we call find_all_indexes
    index_arr = find_all_indexes(text, pattern)
    if len(index_arr) != 0:  # O(1)
        return True  # O(1)
    return False  # O(1)


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
        or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Average case O(n ** 2) - we call find_all_indexes

    index_arr = find_all_indexes(text, pattern)
    try:
        if index_arr[0] != None:  # O(1)
            return index_arr[0]  # O(1)
    except IndexError:
        return None  # O(1)


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Average case O(n ** 2) - where n is the size of the text and the pattern

    indices = []  # O(1)

    for start in range((len(text) - len(pattern) + 1)):  # O(n)
        for offset in range(len(pattern)):  # O(n)
            if text[start + offset] != pattern[offset]:  # O(1)
                break
        else:
            indices.append(start)  # O(1)

    if pattern is '':  # O(1)
        indices.pop()  # O(1)
        return indices  # O(1)

    return indices  # O(1)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
    print(contains('abra cadabra', 'abra'))