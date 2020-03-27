import csv
from FileUtilities.absolutePath import absolute_path
from pprint import pprint

def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        try:
            with open(absolute_path(filepath)) as text_data:
                pprint("1")
                csv_data = csv.DictReader(text_data, delimiter=',')
                pprint("2")
                for row in csv_data:
                    self.data.append(row)
                    pprint("3")
                pprint("4")
        except OSError:
            print('cannot open', filepath)

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects