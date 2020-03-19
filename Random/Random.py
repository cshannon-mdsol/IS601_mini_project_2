from Random.GenNumber import generate_number
from Random.GenNumberSeed import generate_number_seed
from Random.GenNumberListSeed import generate_numbers_list_seed
from Random.ListItem import random_from_list
from Random.ListItemSeed import random_from_list_seed
from Random.NListItem import pick_from_list
from Random.NListItemSeed import pick_from_list_seed


class Random:
    result = 0

    def __init__(self):
        pass

    def gen_num(self, x, y):
        self.result = generate_number(x, y)
        return self.result

    def gen_num_seed(self, x, y, seed_value):
        self.result = generate_number_seed(x, y, seed_value)
        return self.result

    def gen_num_list_seed(self, x, y, seed_value, list_size):
        self.result = generate_numbers_list_seed(x, y, seed_value, list_size)
        return self.result

    def list_item(self, list_array):
        self.result = random_from_list(list_array)
        return self.result

    def list_item_seed(self, list_array, seed_value):
        self.result = random_from_list_seed(list_array, seed_value)
        return self.result

    def n_list_item(self, list_array, how_many_items):
        self.result = pick_from_list(list_array, how_many_items)
        return self.result

    def n_list_item_seed(self, list_array, how_many_items, seed_value):
        self.result = pick_from_list_seed(list_array, how_many_items, seed_value)
        return self.result

