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
        dlist = DiskList()
        dlist.append('0')
        dlist.append('1')
        dlist.append('2')
        dlist.append('3')

        dlist[0] = '10'

        self.assertTrue(dlist[0] == '10' and dlist[1] == '1' and dlist[2] == '2' and dlist[-1] == '3')

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

if __name__ == '__main__':
    unittest.main()
