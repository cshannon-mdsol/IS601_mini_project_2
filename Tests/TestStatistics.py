import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Statistics, Statistics)

    def test_confidence_interval(self):
        pprint("________CI Top________")
        pprint("________CI Bottom________")
        test_data = CsvReader('/Tests/csv/Confidence_Interval.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.confidence_interval_top(self.column1), float(row['ci_top']))
            self.assertEqual(self.Statistics.confidence_interval_bottom(self.column1), float(row['ci_bottom']))
            
    def test_correlation_statistics(self):
        pprint("________Correlation________")
        test_data = CsvReader('/Tests/csv/Correlation.csv').data  
        for row in self.test_data:
            self.assertEqual(self.Statistics.correlation_coefficient(self.column1, self.column2),float(row['correlation']))
            self.assertEqual(self.Statistics.result, float(row['correlation']))

    def test_median_statistics(self):
        pprint("________Median________")
        test_data = CsvReader('/Tests/csv/Subtraction.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.median(self.column1), float(row['median']))
            self.assertEqual(self.Statistics.result, float(row['median']))
            
    def test_mean_statistics(self):
        pprint("________Mean________")
        test_data = CsvReader('/Tests/csv/Mean.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.mean(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.Statistics.result, float(row['mean']))
            
    def test_mode_statistics(self):
        pprint("________Mode________")
        test_data = CsvReader('/Tests/csv/Mode.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.mode(self.column1), float(row['mode']))
            self.assertEqual(self.Statistics.result, float(row['mode']))
            
    def test_population_mean_statistics(self):
        pprint("________Population Mean________")
        test_data = CsvReader('/Tests/csv/PopulationMean.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.population_mean(self.column1), float(row['mean']))
            self.assertEqual(self.Statistics.result, float(row['mean']))

    def test_proportion_statistics(self):
        pprint("________Proportion________")
        test_data = CsvReader('/Tests/csv/Proportion.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.proportion(self.column1), self.column_proportion)
            self.assertEqual(self.Statistics.result, self.column_proportion)

    def test_p_value_statistics(self):
        pprint("________P Value________")
        test_data = CsvReader('/Tests/csv/PValue.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.p_value(self.column1), self.column_zscore)
            self.assertEqual(self.Statistics.result, self.column_zscore)

    def test_standard_deviation_statistics(self):
        pprint("________Std Deviation________")
        test_data = CsvReader('/Tests/csv/StdDeviation.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.stddev(self.column1), float(row['stddev']))
            self.assertEqual(self.Statistics.result, float(row['stddev']))

    def test_variance_statistics(self):
        pprint("________Variance________")
        test_data = CsvReader('/Tests/csv/Variance.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.variance(self.column1), float(row['variance']))
            self.assertEqual(self.Statistics.result, float(row['variance']))

    def test_proportion_variance_statistics(self):
        pprint("________Prop Variance________")
        test_data = CsvReader('/Tests/csv/PropVariance.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.population_proportion_variance(self.column1),
                             float(row['proportion_variance']))
            self.assertEqual(self.Statistics.result, float(row['proportion_variance']))

    def test_z_score_statistics(self):
        pprint("________Z Score________")
        test_data = CsvReader('/Tests/csv/ZScore.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.z_score(self.column1), self.column_zscore)
            self.assertEqual(self.Statistics.result, self.column_zscore)

    def test_sample_mean_statistics(self):
        pprint("________Sample Mean________")
        test_data = CsvReader('/Tests/csv/SampleMean.csv').data
        for row in self.tes_data:
            self.assertEqual(self.Statistics.sample_mean(self.column3), float(row['mean']))
            self.assertEqual(self.Statistics.result, float(row['mean']))

    def test_sample_standard_deviation_statistics(self):
        pprint("_________Sample Std Deviation________")
        test_data = CsvReader('/Tests/csv/SampleStdDeviation.csv').data
        for row in self.test_data:
            self.assertEqual(self.Statistics.sample_stddev(self.column3), float(row['stddev']))
            self.assertEqual(self.Statistics.result, float(row['stddev']))

    def test_sample_variance_statistics(self):
        pprint("________Sample Variance________")
        test_data = CsvReader('/Tests/csv/SampleVariance.csv').data
        for row in self.tes_data:
            self.assertEqual(self.Statistics.sample_variance(self.column3), float(row['variance']))
            self.assertEqual(self.Statistics.result, float(row['variance']))


if __name__ == '__main__':
    unittest.main()
