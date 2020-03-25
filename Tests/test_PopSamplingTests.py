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
    col1_Confidence = [row['CI'] for row in test_ConfidenceInterval]
    col2_Confidence = [row['Z'] for row in test_ConfidenceInterval]


    def setUp(self):
        self.PopSampling = PopSampling()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.PopSampling, PopSampling)

    def test_confidence_interval(self):
        pprint("________Confidence Interval________")
        for row in self.test_ConfidenceInterval:
            theList1 = [self.col1_Confidence]
            theList2 = [self.col2_Confidence]
            theList3 = [ (row['xMean']), (row['nObservations']), (row['sSD'])]
            #pprint(theList3)
            self.PopSampling.confidence_interval_pop(theList1,theList2,theList3)
            #self.assertEqual(self.Statistics.result, float(row['CalculatedMean']))
            #print("Test")


if __name__ == '__main__':
    unittest.main()