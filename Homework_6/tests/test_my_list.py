import unittest

from my_list import MyList

class TestMyList(unittest.TestCase):

    def test_is_empty(self):
        my_list = MyList()
        self.assertTrue(my_list.empty())

    def test_is_empty_false(self):
        my_list = MyList()
        my_list.add(1)
        self.assertFalse(my_list.empty())

    def test_add_item(self):
        my_list = MyList()
        my_list.add(1)
        self.assertNotEqual(my_list[0], None)
        self.assertEqual(my_list[0], 1)

    def test_add_more_items(self):
        my_list = MyList()
        my_list.add(1)
        my_list.add(2)
        self.assertEqual(my_list[0], 1)
        self.assertEqual(my_list[1], 2)

    def test_get_item(self):
        my_list = MyList()
        my_list.add(1)
        my_list.add(3)
        self.assertNotEqual(my_list[1], None)
        self.assertEqual(my_list[1], 3)

    def test_set_item(self):
        my_list = MyList()
        my_list.add(1)
        my_list.add(3)
        my_list[1] = "Otro"
        self.assertNotEqual(my_list[1], None)
        self.assertEqual(my_list[1], "Otro")
        
    def test_size(self):
        my_list = MyList()
        my_list.add(2)
        my_list.add(3)
        my_list.add(2)
        my_list.add(3)
        self.assertEqual(len(my_list), 4)

    def test_passing_args(self):
        my_list = MyList(3, 5, 5, 7)
        self.assertEqual(len(my_list), 4)
        self.assertEqual(my_list[3], 7)

    def test_iterate_my_list(self):
        my_list = MyList(3, 5, 7, ' ', 'errr', True)
        size = 0
        for _ in my_list:
            size += 1
        self.assertEqual(len(my_list), size)
        