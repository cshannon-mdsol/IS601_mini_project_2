from Calculator.Calculator import Calculator
from Statistics.Mean import Mean


class Statistics(Calculator):

    def mean(self, data):
        self.result = Mean(data)
        return self.result
