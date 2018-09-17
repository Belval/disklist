import unittest

from disklist import DiskList

class TestDiskList(unittest.TestCase):
    def test_add(self):
        """
            Test the + operator
        """

        dlist1 = DiskList()
        dlist2 = DiskList()
        dlist1.append('1')
        dlist1.append('2')
        dlist2.append('3')
        dlist2.append('4')

        dlist = dlist1 + dlist2

        self.assertTrue(len(dlist) == 4)

    def test_getitem(self):
        """
            Test the [] operator for getting items
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        self.assertTrue(dlist[0] == '0' and dlist[1] == '1' and dlist[2] == '2' and dlist[-1] == '3')

    def test_setitem(self):
        """
            Test the [] operator for setting items
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        dlist[0] = '10'

        self.assertTrue(dlist[0] == '10' and dlist[1] == '1' and dlist[2] == '2' and dlist[-1] == '3')

    def test_delitem(self):
        """
            Test the [] operator for deleting items
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        del dlist[0]

        self.assertTrue(dlist[0] == '1' and dlist[1] == '2' and dlist[-1] == '3')

    def test_remove(self):
        """
            Test the remove method
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')
        dlist.append('0')

        dlist.remove('0')

        self.assertTrue(dlist[0] == '1' and dlist[1] == '2' and dlist[2] == '3' and dlist[3] == '0')

    def test_pop_without_index(self):
        """
            Test the pop method without index
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        result = dlist.pop()

        self.assertTrue(dlist[0] == '0' and dlist[1] == '1' and dlist[2] == '2' and result == '3' and len(dlist) == 3)

    def test_pop_with_index(self):
        """
            Test the pop method without index
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        result = dlist.pop(2)

        self.assertTrue(dlist[0] == '0' and dlist[1] == '1' and dlist[2] == '3' and result == '2' and len(dlist) == 3)

    def test_index(self):
        """
            Test the index method
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        self.assertTrue(dlist.index('2') == 2)

    def test_index_with_bounds(self):
        """
            Test the index method with bounds
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        self.assertRaises(ValueError, lambda: dlist.index('2', 0, 1))

    def test_clear(self):
        """
            Test the clear method
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')

        dlist.clear()

        self.assertTrue(len(dlist) == 0)

    def test_len(self):
        """
            Test the len() function
        """

        dlist = DiskList()

        self.assertTrue(len(dlist) == 0)

    def test_append(self):
        """
            Test appending new items
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        self.assertTrue(len(dlist) == 4)

    def test_extend(self):
        """
            Test the extend method
        """

        dlist = DiskList()
        dlist.extend(['0', '1', '2', '3'])

        self.assertTrue(len(dlist) == 4)

    def test_insert(self):
        """
            Test inserting new items
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        dlist.insert(1, '10')

        self.assertTrue(len(dlist) == 5 and dlist[1] == '10')

    def test_iteration(self):
        """
            Test iterating through the DiskList
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        result_list = []

        for item in dlist:
            result_list.append(item)

        self.assertTrue(
            result_list[0] == '0' and
            result_list[1] == '1' and
            result_list[2] == '2' and
            result_list[3] == '3'
        )

    def test_count(self):
        """
            Test count method
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('3')
        dlist.append('3')

        self.assertTrue(dlist.count('1') == 1 and dlist.count('3') == 2 and dlist.count('1337') == 0)

    def test_clear_not_empty(self):
        """
            Test clear method
        """

        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        dlist.clear()

        self.assertTrue(len(dlist) == 0)

    def test_clear_empty(self):
        """
            Test clear method when list is empty
        """

        dlist = DiskList()

        dlist.clear()

        self.assertTrue(len(dlist) == 0)

    def test_use_cache(self):
        """
            Test using cache
        """

        dlist = DiskList(cache_size=10)

        l1 = []
        l2 = []
        l3 = []
        l4 = []

        for i in range(100):
            dlist.append(i)
            l1.append(i) 

        for i in dlist:
            l2.append(i)

        for i in dlist:
            l3.append(i)

        l4 = dlist[0:50]
        for i in dlist[50:]:
            l4.append(i)

        self.assertTrue(all([i == j and j == k and k == l for i, j, k, l in zip(l1, l2, l3, l4)]))
    
    def test_use_cache_bigger_than_list(self):
        """
            Test using cache
        """

        dlist = DiskList(cache_size=1000)

        l1 = []
        l2 = []
        l3 = []
        l4 = []

        for i in range(100):
            dlist.append(i)
            l1.append(i) 

        for i in dlist:
            l2.append(i)

        for i in dlist:
            l3.append(i)

        l4 = dlist[0:50]
        for i in dlist[50:]:
            l4.append(i)

        self.assertTrue(all([i == j and j == k and k == l for i, j, k, l in zip(l1, l2, l3, l4)]))
    
    def test_use_cache_of_1(self):
        """
            Test using cache
        """

        dlist = DiskList(cache_size=1)

        l1 = []
        l2 = []
        l3 = []
        l4 = []

        for i in range(100):
            dlist.append(i)
            l1.append(i) 

        for i in dlist:
            l2.append(i)

        for i in dlist:
            l3.append(i)

        l4 = dlist[0:50]
        for i in dlist[50:]:
            l4.append(i)

        self.assertTrue(all([i == j and j == k and k == l for i, j, k, l in zip(l1, l2, l3, l4)]))

    def test_use_cache_of_0(self):
        """
            Test using cache
        """

        dlist = DiskList(cache_size=0)

        l1 = []
        l2 = []
        l3 = []
        l4 = []

        for i in range(100):
            dlist.append(i)
            l1.append(i) 

        for i in dlist:
            l2.append(i)

        for i in dlist:
            l3.append(i)

        l4 = dlist[0:50]
        for i in dlist[50:]:
            l4.append(i)

        self.assertTrue(all([i == j and j == k and k == l for i, j, k, l in zip(l1, l2, l3, l4)]))

if __name__ == '__main__':
    unittest.main()
