import unittest

from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10, 20)
        self.Statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.Statistics.mean(self.testData)
        self.assertEqual(mean, 4.25)


if __name__ == '__main__':
    unittest.main()
