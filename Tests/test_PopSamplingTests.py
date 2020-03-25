import unittest
from PopSampling.SimpleRandom import SimpleRandom
from PopSampling.SystemicSampling import SystematicSampling
from PopSampling.ConIntervalSam import confidence_interval_sam
from PopSampling.MarginError import MarginError
from PopSampling.ConIntervalPop import confidence_interval_pop
from PopSampling.Cochran import Cochran
from PopSampling.UnkSampleSize import UnkSampleSize
from PopSampling.PopSampleSize import PopSampleSize
from PopSampling.PopSampling import PopSampling
from CsvReader.CsvReader import CsvReader

from pprint import pprint

class MyTestCase(unittest.TestCase):


    test_ConfidenceInterval = CsvReader('/Tests/csv/ConfidenceInterval.csv').data


    def setUp(self):
        self.PopSampling = PopSampling()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.PopSampling, PopSampling)

    def test_confidence_interval(self):
        pprint("________Confidence Interval________")
        for row in self.test_ConfidenceInterval:
            pprint(row)
            #self.assertEqual(self.Statistics.mean(theList), float(row['CalculatedMean']))
            #self.assertEqual(self.Statistics.result, float(row['CalculatedMean']))
            print("Test")


if __name__ == '__main__':
    unittest.main()