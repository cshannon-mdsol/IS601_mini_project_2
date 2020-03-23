from random import randint


class ListItem:

    @staticmethod
    def list_item(series):
        length = len(series)
        position = randint(0, length-1)
        return series[position]
