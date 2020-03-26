from Calculator.Calculator import Calculator
from PopSampling.ConfidenceInterval import confidence_interval
from PopSampling.Cochran import cochran
from PopSampling.ConfidenceIntervalKnown import confidence_interval_known
from PopSampling.ConfidenceIntervalUnknown import confidence_interval_unknown

class PopSampling(Calculator):
    data = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []


    def __init__(self):
        super().__init__()

    def confidence_interval(self, data1,data2,data3):
        self.result = confidence_interval(data1,data2,data3)
        return self.result

    def confidence_interval_known(self, data):
        self.result = confidence_interval_known(data)
        return self.result

    def confidence_interval_unknown(self, data):
        self.result = confidence_interval_unknown(data)
        return self.result

    def cochran(self, data1,data2,data3,data4):
        self.result = cochran(data1,data2,data3,data4)
        return self.result

    pass
