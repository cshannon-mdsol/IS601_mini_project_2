import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    test_conf = CsvReader('/Tests/csv/Confidence_Interval.csv').data
    test_corr = CsvReader('/Tests/csv/Correlation.csv').data
    test_med = CsvReader('/Tests/csv/Median.csv').data
    test_mean = CsvReader('/Tests/csv/Mean.csv').data
    test_mode = CsvReader('/Tests/csv/Mode.csv').data
    test_pop_mean = CsvReader('/Tests/csv/PopulationMean.csv').data
    test_prop = CsvReader('/Tests/csv/Proportion.csv').data
    test_p_value = CsvReader('/Tests/csv/PValue.csv').data
    test_stddev = CsvReader('/Tests/csv/StdDeviation.csv').data
    test_var = CsvReader('/Tests/csv/Variance.csv').data
    test_prop_var = CsvReader('/Tests/csv/PropVariance.csv').data
    test_z_score = CsvReader('/Tests/csv/ZScore.csv').data
    test_sam_mean = CsvReader('/Tests/csv/SampleMean.csv').data
    test_sam_stddev = CsvReader('/Tests/csv/SampleStdDeviation.csv').data
    test_sav_var = CsvReader('/Tests/csv/SampleVariance.csv').data

    def setUp(self):
        self.Statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Statistics, Statistics)

    def test_confidence_interval(self):
        pprint("________CI Top________")
        pprint("________CI Bottom________")
        for row in self.test_conf:
            self.assertEqual(self.Statistics.confidence_interval_top(self.column1), float(row['ci_top']))
            self.assertEqual(self.Statistics.confidence_interval_bottom(self.column1), float(row['ci_bottom']))
            
    def test_correlation_statistics(self):
        pprint("________Correlation________")
        for row in self.test_corr:
            self.assertEqual(self.Statistics.correlation_coefficient(self.column1, self.column2),
                             float(row['correlation']))
            self.assertEqual(self.Statistics.result, float(row['correlation']))

    def test_median_statistics(self):
        pprint("________Median________")
        for row in self.test_med:
            self.assertEqual(self.Statistics.median(self.column1), float(row['median']))
            self.assertEqual(self.Statistics.result, float(row['median']))
            
    def test_mean_statistics(self):
        pprint("________Mean________")
        for row in self.test_mean:
            self.assertEqual(self.Statistics.mean(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.Statistics.result, float(row['mean']))
            
    def test_mode_statistics(self):
        pprint("________Mode________")
        for row in self.test_mode:
            self.assertEqual(self.Statistics.mode(self.column1), float(row['mode']))
            self.assertEqual(self.Statistics.result, float(row['mode']))
            
    def test_population_mean_statistics(self):
        pprint("________Population Mean________")
        for row in self.test_pop_mean:
            self.assertEqual(self.Statistics.population_mean(self.column1), float(row['mean']))
            self.assertEqual(self.Statistics.result, float(row['mean']))

    def test_proportion_statistics(self):
        pprint("________Proportion________")
        for row in self.test_prop:
            self.assertEqual(self.Statistics.proportion(self.column1), self.column_proportion)
            self.assertEqual(self.Statistics.result, self.column_proportion)

    def test_p_value_statistics(self):
        pprint("________P Value________")
        for row in self.test_p_value:
            self.assertEqual(self.Statistics.p_value(self.column1), self.column_zscore)
            self.assertEqual(self.Statistics.result, self.column_zscore)

    def test_standard_deviation_statistics(self):
        pprint("________Std Deviation________")
        for row in self.test_stddev:
            self.assertEqual(self.Statistics.stddev(self.column1), float(row['stddev']))
            self.assertEqual(self.Statistics.result, float(row['stddev']))

    def test_variance_statistics(self):
        pprint("________Variance________")
        for row in self.test_var:
            self.assertEqual(self.Statistics.variance(self.column1), float(row['variance']))
            self.assertEqual(self.Statistics.result, float(row['variance']))

    def test_proportion_variance_statistics(self):
        pprint("________Prop Variance________")
        for row in self.test_prop_var:
            self.assertEqual(self.Statistics.population_proportion_variance(self.column1),
                             float(row['proportion_variance']))
            self.assertEqual(self.Statistics.result, float(row['proportion_variance']))

    def test_z_score_statistics(self):
        pprint("________Z Score________")
        for row in self.test_z_score:
            self.assertEqual(self.Statistics.z_score(self.column1), self.column_zscore)
            self.assertEqual(self.Statistics.result, self.column_zscore)

    def test_sample_mean_statistics(self):
        pprint("________Sample Mean________")
        for row in self.test_sam_mean:
            self.assertEqual(self.Statistics.sample_mean(self.column3), float(row['mean']))
            self.assertEqual(self.Statistics.result, float(row['mean']))

    def test_sample_standard_deviation_statistics(self):
        pprint("_________Sample Std Deviation________")
        for row in self.test_sam_stddev:
            self.assertEqual(self.Statistics.sample_stddev(self.column3), float(row['stddev']))
            self.assertEqual(self.Statistics.result, float(row['stddev']))

    def test_sample_variance_statistics(self):
        pprint("________Sample Variance________")
        for row in self.tes_sam_var:
            self.assertEqual(self.Statistics.sample_variance(self.column3), float(row['variance']))
            self.assertEqual(self.Statistics.result, float(row['variance']))


if __name__ == '__main__':
    unittest.main()
