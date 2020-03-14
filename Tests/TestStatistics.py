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
            self.assertEqual(self.Statistics.mode(self.column1), float(row['mode']))
            self.assertEqual(self.Statistics.result, float(row['mode']))

    def test_variance_statistics(self):
        pprint("________Variance________")
        for row in self.test_var:
            self.assertEqual(self.Statistics.variance(self.column1), float(row['variance']))
            self.assertEqual(self.Statistics.result, float(row['variance']))

    def test_standard_deviation_statistics(self):
        pprint("________Std Deviation________")
        for row in self.test_stddev:
            self.assertEqual(self.Statistics.stddev(self.column1), float(row['stddev']))
            self.assertEqual(self.Statistics.result, float(row['stddev']))

    def test_quartiles_statistics(self):
        pprint("________Quartiles________")
        for row in self.test_quar:
            self.assertEqual(self.Statistics.quartiles)
            self.assertEqual(self.Statistics.result)

    def test_skewness_statistics(self):
        pprint("________Slewness________")
        for row in self.test_skew:
            self.assertEqual(self.Statistics.skewness)
            self.assertEqual(self.Statistics.result)

    def test_sample_correlation_statistics(self):
        pprint("________Sample Correlation________")
        for row in self.test_sam_corr:
            self.assertEqual(self.Statistics.sample_correlation)
            self.assertEqual(self.Statistics.result)

    def test_population_correlation_statistics(self):
        pprint("________Population Correlation________")
        for row in self.test_pop_corr:
            self.assertEqual(self.Statistics.population_correlation)
            self.assertEqual(self.Statistics.result)

    def test_z_score_statistics(self):
        pprint("________Z Score________")
        for row in self.test_z_score:
            self.assertEqual(self.Statistics.z_score(self.column1), self.column_zscore)
            self.assertEqual(self.Statistics.result, self.column_zscore)

    def test_mean_deviation_statistics(self):
        pprint("________Mean Deviation________")
        for row in self.test_mean_dev:
            self.assertEqual(self.Statistics.mean_deviation)
            self.assertEqual(self.Statistics.result)


if __name__ == '__main__':
    unittest.main()
