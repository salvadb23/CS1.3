from linkedlist import LinkedList


class ArraySet:
    def __init__(self, elements=None):
        self.size = 0
        self.elements = []

        if elements is not None:
            for item in elements:
                self.add(item)

    def __repr__(self):
        return "Set size: {}".format(self.size)

    def contains(self, element):
        '''Checks to see if an element is within the set'''
        # O(n) where N is the size of the list
        return element in self.elements

    def add(self, element):
        '''Adds an element to the set'''
        # O(n) where N is the size of the list
        if self.contains(element) is False:
            self.size += 1
            self.elements.append(element)

    def remove(self, element):
        '''Removes an element from the set'''
        # O(n) - where N is the number of elements
        if self.contains(element):
            self.elements.remove(element)
            self.size -= 1
        else:
            raise KeyError("{} is not in this set".format(element))

    def union(self, other_set):
        '''Joins the two sets into one'''
        for item in other_set.elements:
            self.add(item)
        return self

    def intersection(self, other_set):
        '''Find what the two sets have in common'''
        new_set = ArraySet()
        for item in other_set.elements:
            if self.contains(item):
                new_set.add(item)
        return new_set

    def difference(self, other_set):
        '''Finds the items the sets don't have in common '''
        set_cp = other_set
        for item in self.elements:
            if set_cp.contains(item):
                set_cp.remove(item)
        return set_cp

    def is_sub_set(self, other_set):
        '''Determines if all the items in the original set are within the set that is passed'''
        sub_set = []
        for item in self.elements:
            if other_set.contains(item):
                sub_set.append(item)
        return sub_set == self.elements


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedSet(LinkedList):

    def __init__(self, iterable=None):
        super(LinkedSet, self).__init__()

        if iterable is not None:
            for item in iterable:
                self.add(item)
            
        self.list_of_nodes = self.items()

    def contains(self, element):
        '''Verifies an element is within the set'''
        return True if self.find(lambda node: node == element) is not None else False

    def add(self, element):
        '''Adds an item to the set'''
        if self.contains(element) is False:
            self.append(element)

        return self

    def remove(self, element):
        '''Removes item from the set'''
        self.delete(element)

    def union(self, other_set):

        for item in other_set.list_of_nodes:
            self.add(item)

        return self

    def intersection(self, other_set):
        new_set = LinkedSet()

        for item in other_set.list_of_nodes:
            if self.contains(item):
                new_set.add(item)

        return new_set

    def difference(self, other_set):
        set_cp = other_set

        for item in self.list_of_nodes:
            if set_cp.contains(item):
                set_cp.remove(item)

        return set_cp

    def is_subset(self, other_set):
        sub_set = []
        node_list = self.items()

        for item in node_list:
            if other_set.contains(item) is not True:
                return False

        return True


set_one = LinkedSet([1,1,1,1,1,2])
print(set_one)