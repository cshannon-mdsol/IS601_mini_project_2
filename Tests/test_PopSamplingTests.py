import unittest
 from PopSampling.SimpleRandom import SimpleRandom
 from PopSampling.SystemicSampling import SystematicSampling
 from PopSampling.ConIntervalSam import ConfidenceIntervalSam
 from PopSampling.MarginError import MarginError
 from PopSampling.ConIntervalPop import ConfidenceIntervalPop
 from PopSampling.Cochran import Cochran
 from PopSampling.UnkSampleSize import UnkSampleSize
 from PopSampling.PopSampleSize import PopSampleSize

 
  class MyTestCase(unittest.TestCase):
     def setUp(self) -> None:
         self.testData
