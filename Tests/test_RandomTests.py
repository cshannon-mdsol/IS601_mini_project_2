import unittest
from Random.Random import rand_num
from Random.GenNumber import GenNumber
from Random.GenNumberSeed import GenNumberSeed
from Random.GenNumberListSeed import GenNumberListSeed
from Random.ListItem import ListItem
from Random.ListItemSeed import ListItemSeed
from Random.NListItem import NListItem
from Random.NListItemSeed import NListItemSeed


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = rand_num(250, 1, 1000, 55)

    def test_gen_num(self):
        result = GenNumber.rand_num(1, 1000)
        self.assertEqual(isinstance(result, int), True)

    def test_gen_num_float(self):
        result = GenNumber.rand_float(1, 1000)
        self.assertEqual(isinstance(result, float), True)

    def test_gen_num_seed(self):
        result = GenNumberSeed.rand_num(1, 1000, 55)
        result2 = GenNumberSeed.rand_num(1, 1000, 55)
        self.assertEqual(result, result2)

    def test_gen_num_seed_float(self):
        result = GenNumberSeed.rand_float(1, 1000, 55)
        result2 = GenNumberSeed.rand_float(1, 1000, 55)
        self.assertEqual(result, result2)

    def test_gen_num_list_seed(self):
        result = GenNumberListSeed.list_num(1, 1000, 55, 20)
        result2 = GenNumberListSeed.list_num(1, 1000, 55, 20)
        self.assertEqual(result, result2)

    def test_gen_num_list_seed_float(self):
        result = GenNumberListSeed.list_float(1, 1000, 55, 20)
        result2 = GenNumberListSeed.list_float(1, 1000, 55, 20)
        self.assertEqual(result, result2)

    def test_list_item(self):
        series = GenNumberListSeed.list_num(1, 1000, 55, 20)
        result = ListItem.list_item(series)
        self.assertEqual(result, 55)

    def test_rand_list_seed(self):
        series = GenNumberListSeed.list_num(1, 1000, 55, 20)
        result = ListItemSeed.rand_list_seed(5, series)
        self.assertEqual(result, 5)

    def test_pick_from_list(self):
        series = GenNumberListSeed.list_num(1, 1000, 55, 20)
        result = NListItem.pick_from_list(series, 3)
        self.assertEqual(result, [1, 3, 7, 9])

    def test_pick_from_list_seed(self):
        series = GenNumberListSeed.list_num(1, 1000, 55, 20)
        result = NListItemSeed.pick_from_list_seed(3, series, 5)
        self.assertEqual(result, [15, 20, 25, 30, 35])

if __name__ == '__main__':
    unittest.main()