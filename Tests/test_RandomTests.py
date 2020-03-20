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
        result = GenNumber.rand_num()
        self.assertEqual(isinstance(result, int), True)

    def test_gen_num_float(self):
        result = GenNumber.rand_float()
        self.assertEqual(isinstance(result, float), True)

    def test_gen_num_seed(self):
        result = GenNumberSeed.rand_num()
        result2 = GenNumberSeed.rand_num()
        self.assertEqual(result, result2)

    def test_gen_num_seed_float(self):
        result = GenNumberSeed.rand_float()
        result2 = GenNumberSeed.rand_float()
        self.assertEqual(result, result2)

    def test_gen_num_list_seed(self):
        result = GenNumberListSeed.list_num()
        result2 = GenNumberListSeed.list_num()
        self.assertEqual(result, result2)

    def test_gen_num_list_seed_float(self):
        result = GenNumberListSeed.list_float()
        result2 = GenNumberListSeed.list_float()
        self.assertEqual(result, result2)

    def test_list_item(self):
        series = GenNumberListSeed.list_num()
        result = ListItem.list_item(series)
        self.assertEqual(result, )

    def test_rand_list_seed(self):
        series = GenNumberListSeed.list_num(0, 10, 5, 4)
        result = ListItemSeed.rand_list_seed(3, series)
        self.assertEqual(result, 1)

    def test_pick_from_list(self):
        series = GenNumberListSeed.list_num()
        result = NListItem.pick_from_list(series, )
        self.assertEqual(result, [])

    def test_pick_from_list_seed(self):
        series = GenNumberListSeed.list_num(0, 10, 10, 3)
        result = NListItemSeed.pick_from_list_seed(3, series, 5)
        self.assertEqual(result, [9, 8, 9, 9, 8])


if __name__ == '__main__':
    unittest.main()