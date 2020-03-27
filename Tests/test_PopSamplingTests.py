import unittest
# from PopSampling.SimpleRandom import simple_random
# from PopSampling.SystemicSampling import SystematicSampling
# from PopSampling.ConIntervalSam import confidence_interval_sam
# from PopSampling.MarginError import MarginError
# from PopSampling.ConfidenceInterval import confidence_interval
# from PopSampling.Cochran import cochran
# from PopSampling.UnkSampleSize import UnkSampleSize
# from PopSampling.PopSampleSize import PopSampleSize
from PopSampling.PopSampling import PopSampling
from CsvReader.CsvReader import CsvReader

from PopSampling.ConfidenceIntervalKnown import confidence_interval_known
from PopSampling.ConfidenceIntervalUnknown import confidence_interval_unknown

from pprint import pprint


class MyTestCase(unittest.TestCase):
    test_RandData = CsvReader('/Tests/csv/Rand_Data.csv').data
    col2_value1 = [row['value1'] for row in test_RandData]

    ConfidenceIntervalMargin = CsvReader('/Tests/csv/ConfidenceIntervalMargin.csv').data
    test_CIUnknownKnown = CsvReader('/Tests/csv/CIUnknownKnown.csv').data
    # col1_Confidence = [row['Value 1'] for row in test_ConfidenceInterval]
    test_mean = CsvReader('/Tests/csv/Mean.csv').data
    # col2_Confidence = [row['Z'] for row in test_ConfidenceInterval]
    # col3_Confidence = [row['xMean'] for row in test_ConfidenceInterval]
    # col4_Confidence = [row['nObservations'] for row in test_ConfidenceInterval]
    # col5_Confidence = [row['sSD'] for row in test_ConfidenceInterval]
    test_cochran = CsvReader('/Tests/csv/Cochran.csv').data
    test_simple_random_file = CsvReader('/Tests/csv/SimpleRandom.csv').data

    test_ConfidenceIntervals = CsvReader('/Tests/csv/ConfidenceIntervals.csv').data
    col1_ConfidenceIntervals= [row['value1'] for row in test_ConfidenceIntervals]

    def setUp(self):
        self.PopSampling = PopSampling()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.PopSampling, PopSampling)

    def test_simple_random(self):
        pprint("________Simple Random________")
        for row in self.test_simple_random_file:
            series = [row['V1'], row['V2'], row['V3'], row['V4'], row['V5']]
            val1 = self.PopSampling.simple_random(series, int(row['PickHowMany']))

            # check that the returned items equal the number requested
            self.assertEqual(len(val1), int(row['PickHowMany']))

    def test_systematic_sampling(self):
        pprint("________Systematic Sampling________")
        for row in self.test_simple_random_file:
            series = [row['V1'], row['V2'], row['V3'], row['V4'], row['V5']]
            val1 = self.PopSampling.systematic_sampling(series, int(row['PickHowMany']), int(row['Interval']))

            # check that the returned items equal the number requested
            self.assertEqual(len(val1), int(row['PickHowMany']))

    def test_confidence_interval(self):
        pprint("________Confidence Interval________")
        for row in self.test_ConfidenceIntervals:
            theList = []
            for keys in row.keys():
                if keys == "ci":
                    continue
                theList.append(int(row[keys]))
            self.assertEqual(self.PopSampling.confidence_intervals(theList),str(row['ci']))
            #self.assertEqual(self.PopSampling.result,str(row['margin']))


    def test_ci_Unknow_Known(self):
        pprint("________Confidence Interval Unknown/Known________")
        for row in self.test_CIUnknownKnown:
            self.assertEqual(self.PopSampling.confidence_interval_known(self.col2_value1), float(row['ci_known']))
            self.assertEqual(self.PopSampling.confidence_interval_unknown(self.col2_value1), float(row['ci_unknown']))

    def test_confidence_interval_marginoferror(self):
        pprint("________Margin Of Error________")
        for row in self.ConfidenceIntervalMargin:
            self.PopSampling.ci_margin_error(int(row['n']), int(row['x']), int(row['s']))
            self.assertEqual(self.PopSampling.result, float(row['mofe']))

    def test_Cochran(self):
        pprint("________Cochran________")
        for row in self.test_cochran:
            self.PopSampling.cochran(float(row['p']), float(row['q']), float(row['z']), float(row['e']))
            self.assertEqual(self.PopSampling.result, float(row['a']))
            # print("Test")


if __name__ == '__main__':
    unittest.main()
