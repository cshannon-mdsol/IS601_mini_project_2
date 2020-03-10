from Calculator.calculator import Calculator
from Statistics.mean import mean


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result
