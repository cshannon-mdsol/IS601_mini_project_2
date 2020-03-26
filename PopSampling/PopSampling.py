from Calculator.Calculator import Calculator
from PopSampling.ConfidenceInterval import confidence_interval
from PopSampling.Cochran import cochran
from PopSampling.ConfidenceIntervalTop import confidence_interval_top
from PopSampling.ConfidenceIntervalBottom import confidence_interval_bottom
from PopSampling.SimpleRandom import simple_random
from PopSampling.SystematicSampling import systematic_sampling


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

    def confidence_interval(self, data1, data2, data3):
        self.result = confidence_interval(data1, data2, data3)
        return self.result

    def confidence_interval_top(self, data):
        self.result = confidence_interval_top(data)
        return self.result

    def confidence_interval_bottom(self, data):
        self.result = confidence_interval_bottom(data)
        return self.result

    def cochran(self, data1, data2, data3, data4):
        self.result = cochran(data1, data2, data3, data4)
        return self.result

    pass
