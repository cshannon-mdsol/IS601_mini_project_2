import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Calculator, Calculator)

    def test_subtraction(self):
        print("________Subtraction________")
        test_data = CsvReader('/Tests/csv/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.Calculator.Subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.Calculator.result, int(row['Result']))

            print(row['Value 2'], '-', row['Value 1'], '=', self.Calculator.result)

    def test_addition(self):
        print("________Addition________")
        test_data = CsvReader('/Tests/csv/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.Calculator.Add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.Calculator.result, int(row['Result']))

            print(row['Value 2'], '+', row['Value 1'], '=', self.Calculator.result)

    def test_multiplication(self):
        print("________Multiplication________")
        test_data = CsvReader('/Tests/csv/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.Calculator.Multiply(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.Calculator.result, float(row['Result']))

            print(row['Value 2'], '*', row['Value 1'], '=', self.Calculator.result)

    def test_division(self):
        print("________Division________")
        test_data = CsvReader('/Tests/csv/Division.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.Calculator.Divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertAlmostEqual(self.Calculator.result, float(row['Result']))

            print(row['Value 2'], '/', row['Value 1'], '=', self.Calculator.result)

    def test_square(self):
        print("________Square________")
        test_data = CsvReader('/Tests/csv/Square.csv').data
        for row in test_data:
            self.Calculator.Square(row['Value 1'])
            self.assertEqual(self.Calculator.result, int(row['Result']))

            print(row['Value 1'], '^2', '=', self.Calculator.result)

    def test_squareroot(self):
        print("________Square Root________")
        test_data = CsvReader('/Tests/csv/Square_Root.csv').data
        for row in test_data:
            self.Calculator.SqRoot(int(row['Value 1']))
            self.assertAlmostEqual(self.Calculator.result, float(row['Result']))

            print('√', row['Value 1'], '=', self.Calculator.result)


if __name__ == '__main__':
    unittest.main()
