from Calculator.Calculator import Calculator
from PopSampling.CIMarginError import cimarginerror
from PopSampling.Cochran import cochran
from PopSampling.ConfidenceIntervalKnown import confidence_interval_known
from PopSampling.ConfidenceIntervalUnknown import confidence_interval_unknown
from PopSampling.SimpleRandom import simple_random
from PopSampling.SystematicSampling import systematic_sampling
from PopSampling.ConfidenceIntervals import confidence_intervals


class PopSampling(Calculator):
    data = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []

    def __init__(self):
        super().__init__()

    def simple_random(self, x, y):
        self.result = simple_random(x, y)
        return self.result

    def systematic_sampling(self, x, y, z):
        self.result = systematic_sampling(x, y, z)
        return self.result

    def confidence_intervals(self, data):
        self.result = confidence_intervals(data)
        return self.result

    def ci_margin_error(self, data1, data2, data3):
        self.result = cimarginerror(data1, data2, data3)
        return self.result

    def cochran(self, data1, data2, data3, data4):
        self.result = cochran(data1, data2, data3, data4)
        return self.result

    def confidence_interval_known(self, data):
        self.result = confidence_interval_known(data)
        return self.result

    def confidence_interval_unknown(self, data):
        self.result = confidence_interval_unknown(data)
        return self.result

    pass
