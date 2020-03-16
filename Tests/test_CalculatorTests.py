import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Calculator = Calculator()
        print("Hello")

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Calculator, Calculator)

    def test_subtraction(self):
        pprint("________Subtraction________")
        test_data = CsvReader('/Tests/csv/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.Calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.Calculator.result, int(row['Result']))

    def test_addition(self):
        pprint("________Addition________")
        test_data = CsvReader('/Tests/csv/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.Calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.Calculator.result, int(row['Result']))

    def test_multiplication(self):
        pprint("________Multiplication________")
        test_data = CsvReader('/Tests/csv/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.Calculator.multiply(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.Calculator.result, float(row['Result']))

    def test_division(self):
        pprint("________Division________")
        test_data = CsvReader('/Tests/csv/Division.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.Calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertAlmostEqual(self.Calculator.result, float(row['Result']))

    def test_square(self):
        pprint("________Square________")
        test_data = CsvReader('/Tests/csv/Square.csv').data
        for row in test_data:
            self.Calculator.square(row['Value 1'])
            self.assertEqual(self.Calculator.result, int(row['Result']))

    def test_squareroot(self):
        pprint("________Square Root________")
        test_data = CsvReader('/Tests/csv/Square_Root.csv').data
        for row in test_data:
            self.Calculator.sqroot(int(row['Value 1']))
            self.assertAlmostEqual(self.Calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()
