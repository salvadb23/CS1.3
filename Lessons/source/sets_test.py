from sets import ArraySet, LinkedSet
import unittest


class ArraySetTest(unittest.TestCase):

    def test_init(self):
        list_set = ArraySet()
        assert list_set.size is 0

    def test_init_with_list(self):
        list_set = ArraySet([1, 2, 3])
        assert list_set.size is 3
        assert list_set.contains(2)

    def test_size(self):
        list_set = ArraySet()
        assert list_set.size is 0
        list_set.add(1)
        assert list_set.size is 1
        list_set.add(2)
        assert list_set.size is 2
        list_set.add(3)
        assert list_set.size is 3

    def test_add(self):
        list_set = ArraySet()
        list_set.add(3)
        assert list_set.size is 1
        list_set.add(2)
        assert list_set.size is 2
        list_set.add(2)
        assert list_set.size is 2

    def test_remove(self):
        list_set = ArraySet([1, 2, 3])
        assert list_set.size is 3
        list_set.remove(2)
        assert list_set.size is 2

    def test_union(self):
        set_one = ArraySet([1, 2, 3, 4])
        assert set_one.size is 4
        set_two = ArraySet([1, 2, 3, 4, 5, 4, 5, 3, 5, 6, 7])
        set_one.union(set_two)
        assert set_one.size is 7

    def test_intersection(self):
        set_one = ArraySet(["apple", "fruit", "pear"])
        set_two = ArraySet(["apple", "fruit", "pear", "orange"])
        new_set = set_one.intersection(set_two)
        assert new_set.elements == [
            "apple", "fruit", "pear"]
        set_one = ArraySet([1, 2, 3, 4])
        set_two = ArraySet([2, 31, 2, 31, 2, 1, 2, 3, 4])
        new_set = set_one.intersection(set_two)
        assert new_set.elements == [2, 1, 3, 4]

    def test_difference(self):

        set_one = ArraySet(["apple", "fruit", "pear"])
        set_two = ArraySet(["apple", "fruit", "pear", "orange"])
        new_set = set_one.difference(set_two)
        assert new_set.elements == ["orange"]

        set_one = ArraySet([1, 2, 3, 4])
        set_two = ArraySet([2, 31, 2, 31, 2, 1, 2, 3, 4])
        new_set = set_one.difference(set_two)
        assert new_set.elements == [31]

    def test_is_sub_set(self):
        set_one = ArraySet(["apple", "fruit", "pear"])
        set_two = ArraySet(["apple", "fruit", "pear", "orange"])
        is_subset = set_one.is_sub_set(set_two)
        assert is_subset is True

        set_one = ArraySet(["watermelon", "apple", "pear"])
        set_two = ArraySet(["pear", "grape", "orange"])

        is_subset = set_one.is_sub_set(set_two)
        assert is_subset is False


class LinkSetTest(unittest.TestCase):


    def test_init(self):
        link_set = LinkedSet([1,2,3,4,5])
        assert link_set.size == 5
        
        
        
    def test_contains(self):
        link_set = LinkedSet([1,2,3,4,5])
        assert link_set.contains(2) is True
        assert link_set.contains(1000) is False
        assert link_set.size is 5
    
        

    def test_add(self):
        link_set = LinkedSet([1,2,3,4,5])
        assert link_set.size is 5
        link_set.add(6)
        assert link_set.size is 6
        assert link_set.contains(6) is True

    def test_remove(self):
        link_set = LinkedSet([1,2,3,4,5])
        link_set.remove(4)
        assert link_set.size is 4
        assert link_set.contains(4) is False

    def test_union(self):
        link_set = LinkedSet([1,2,3,4,5])
        link_set_two = LinkedSet([1,2,3,4,5,6,7,8,9,10,11])
        combined_sets = link_set.union(link_set_two)
        combined_sets.size is 10
        combined_sets.list_of_nodes = [1,2,3,4,5,6,7,8,9,10,11]

    def test_intersection(self):
        link_set = LinkedSet([1,2,3,4,5])
        link_set_two = LinkedSet([1,2,3,4,5,6,7,8,9,10,11])
        combined_sets = link_set.intersection(link_set_two)
        combined_sets.size is 5
        combined_sets.list_of_nodes = [1,2,3,4,5]


    def test_difference(self):
        link_set = LinkedSet([1,2,3,4,5])
        link_set_two = LinkedSet([1,2,3,4,5,6,7,8,9,10,11])
        combined_sets = link_set.difference(link_set_two)
        combined_sets.size is 6
        combined_sets.list_of_nodes = [6,7,8,9,10,11]

    def test_is_subset(self):
        link_set = LinkedSet([1,2,3,4,5,2])
        link_set_two = LinkedSet([1,2,3,4,5,6,7,8,9,10,11])
        assert link_set.is_subset(link_set_two) is True
        link_set.add(39)
        assert link_set.is_subset(link_set_two) is False
        print(link_set)
        

if __name__ == '__main__':
    unittest.main()