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
        self.testData = rand_num(1, 1000, 250, 55)

    def test_gen_num(self):
        print("________Generate Random Int________")
        result = GenNumber.rand_num(1, 1000)
        self.assertEqual(isinstance(result, int), True)

    def test_gen_num_float(self):
        print("________Generate Random Float________")
        result = GenNumber.rand_float(1, 1000)
        self.assertEqual(isinstance(result, float), True)

    def test_gen_num_seed(self):
        print("________Generate Random w/ Seed Int________")
        result = GenNumberSeed.rand_num(1, 1000, 55)
        result2 = GenNumberSeed.rand_num(1, 1000, 55)
        self.assertEqual(result, result2)

    def test_gen_num_seed_float(self):
        print("________Generate Random w/ Seed Float________")
        result = GenNumberSeed.rand_float(1, 1000, 55)
        result2 = GenNumberSeed.rand_float(1, 1000, 55)
        self.assertEqual(result, result2)

    def test_gen_num_list_seed(self):
        print("________List Random Number w/ Seed Int________")
        result = GenNumberListSeed.list_num(1, 1000, 20, 55)
        result2 = GenNumberListSeed.list_num(1, 1000, 20, 55)
        self.assertEqual(result, result2)

    def test_gen_num_list_seed_float(self):
        print("________List Random Number w/ Seed Float________")
        result = GenNumberListSeed.list_float(1, 1000, 20, 55)
        result2 = GenNumberListSeed.list_float(1, 1000, 20, 55)
        self.assertEqual(result, result2)

    def test_list_item(self):
        print("________Generate Random from list________")
        series = GenNumberListSeed.list_num(1, 1000, 20, 55)
        result = ListItem.list_item(series)
        self.assertEqual(result, 888)

    def test_rand_list_seed(self):
        print("________Generate Random from list w/ Seed________")
        series = GenNumberListSeed.list_num(1, 1000, 20, 55)
        result = ListItemSeed.rand_list_seed(series, 55)
        self.assertEqual(result, 201)

    def test_pick_from_list(self):
        print("________Pick from list________")
        series = GenNumberListSeed.list_num(1, 1000, 20, 55)
        result = NListItem.pick_from_list(series, 3)
        self.assertEqual(result, [])

    def test_pick_from_list_seed(self):
        print("________Pick from list w/ Seed________")
        series = GenNumberListSeed.list_num(1, 1000, 20, 55)
        result = NListItemSeed.pick_from_list_seed(series, 3, 55)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
