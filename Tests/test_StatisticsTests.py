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
            theList = [row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5'], row['Value6'],
                       row['Value7']]
            self.assertEqual(self.Statistics.mean(theList), float(row['CalculatedMean']))
            self.assertEqual(self.Statistics.result, float(row['CalculatedMean']))
            print(self.Statistics.result, " equals ", row['CalculatedMean'])

    def test_mean_deviation_statistics(self):
        pprint("________Mean Deviation________")
        for row in self.test_mean_dev:
            theList = [row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5'], row['Value6'],
                       row['Value7']]
            self.assertEqual(self.Statistics.meandeviation(theList), float(row['CalculatedMeanDeviation']))
            self.assertEqual(self.Statistics.result, float(row['CalculatedMeanDeviation']))
            print(self.Statistics.result, " equals ", row['CalculatedMeanDeviation'])

    def test_median_statistics(self):
        pprint("________Median________")
        for row in self.test_med:
            theList = []

            for keys in row.keys():
                if keys != "CalculatedMedian":
                    if row[keys] != "-":
                        theList.append(float(row[keys]))

            self.assertEqual(self.Statistics.median(theList), float(row['CalculatedMedian']))
            self.assertEqual(self.Statistics.result, float(row['CalculatedMedian']))
            print(self.Statistics.result, " equals ", float(row['CalculatedMedian']))

    def test_mode_statistics(self):
        pprint("________Mode________")
        for row in self.test_mode:
            self.assertEqual(self.Statistics.mode(self.column1), float(row['mode']))
            self.assertEqual(self.Statistics.result, float(row['mode']))

    def test_mode_statistics(self):
        pprint("________Median Deviation________")
        for row in self.test_mode:
            theList = []

            for keys in row.keys():
                if keys != "CalculatedMode":
                    if row[keys] != "-":
                        theList.append(int(row[keys]))

            if row['CalculatedMode'] != "No mode found":
                self.assertEqual(self.Statistics.mode(theList), int(row['CalculatedMode']))
                self.assertEqual(self.Statistics.result, float(row['CalculatedMode']))
                print(self.Statistics.result, " equals ", int(row['CalculatedMode']))
            else:
                self.assertEqual(self.Statistics.mode(theList), (row['CalculatedMode']))
                self.assertEqual(self.Statistics.result, (row['CalculatedMode']))
                print(self.Statistics.result, " equals ", (row['CalculatedMode']))

    def test_variance_statistics(self):
        for row in self.test_mode:
            pprint(row['variance'])
        self.assertEqual(self.statistics.variance(self.column1), float(row['variance']))
        self.assertEqual(self.statistics.result, float(row['variance']))



if __name__ == '__main__':
    unittest.main()
