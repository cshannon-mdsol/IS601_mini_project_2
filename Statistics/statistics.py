from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.StandardDeviation import stddev
from Statistics.Quartiles import quartiles
from Statistics.Skewness import skewness
from Statistics.SampleCorrelation import sample_correlation
from Statistics.PopulationCorrelation import population_correlation
from Statistics.ZScore import z_score
from Statistics.MeanDeviation import mean_deviation


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def quartiles(self, data):
        self.result = quartiles(data)
        return self.result

    def skewness(self, data):
        self.result = skewness(data)
        return self.result

    def sample_correlation(self, data):
        self.result = sample_correlation(data)
        return self.result

    def population_correlation(self, data):
        self.result = population_correlation(data)
        return self.result

    def z_score(self, data):
        self.result = z_score(data)
        return self.result

    def mean_deviation(self, data):
        self.result = mean_deviation(data)
        return self.result

