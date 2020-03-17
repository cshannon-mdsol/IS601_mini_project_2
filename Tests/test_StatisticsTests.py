import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    test_mean = CsvReader('/Tests/csv/Mean.csv').data
    test_med = CsvReader('/Tests/csv/Median.csv').data
    test_mode = CsvReader('/Tests/csv/Mode.csv').data
    test_var = CsvReader('/Tests/csv/Variance.csv').data
    test_stddev = CsvReader('/Tests/csv/StdDeviation.csv').data
    test_quar = CsvReader('/Tests/csv/Quartiles.csv').data
    test_skew = CsvReader('/Tests/csv/Skewness.csv').data
    test_sam_corr = CsvReader('/Tests/csv/SampleCorrelation.csv').data
    test_pop_corr = CsvReader('/Tests/csv/PopulationCorrelation.csv').data
    test_z_score = CsvReader('/Tests/csv/ZScore.csv').data
    test_mean_dev = CsvReader('/Tests/csv/MeanDeviation.csv').data

    def setUp(self):
        self.Statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Statistics, Statistics)

    def test_mean_statistics(self):
        pprint("________Mean________")
        for row in self.test_mean:
            self.assertEqual(self.Statistics.mean(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.Statistics.result, float(row['mean']))

    def test_median_statistics(self):
        pprint("________Median________")
        for row in self.test_med:
            self.assertEqual(self.Statistics.median(self.column1), float(row['median']))
            self.assertEqual(self.Statistics.result, float(row['median']))

    def test_mode_statistics(self):
        pprint("________Mode________")
        for row in self.test_mode:
            pprint(float(row['mode']))
            self.assertEqual(self.Statistics.mode(self.column1), float(row['mode']))
            self.assertEqual(self.Statistics.result, float(row['mode']))
            pprint(float(row['mode']))




if __name__ == '__main__':
    unittest.main()
