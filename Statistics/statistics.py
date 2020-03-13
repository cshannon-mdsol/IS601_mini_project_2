from Calculator.Calculator import Calculator
from Statistics.ConfidenceIntervalBottom import confidence_interval_bottom
from Statistics.ConfidenceIntervalTop import confidence_interval_top
from Statistics.CorrelationCoefficient import correlation
from Statistics.Median import median
from Statistics.Mean import mean
from Statistics.Mode import mode
from Statistics.PValue import p_value
from Statistics.PopulationMean import population_mean
from Statistics.Proportion import proportion
from Statistics.StandardDeviation import stddev
from Statistics.Variance import variance
from Statistics.VarianceOfPopulationProportion import variance_of_population_proportion
from Statistics.ZScore import z_score


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def confidence_interval_bottom(self, data):
        self.result = confidence_interval_bottom(data)
        return self.result

    def confidence_interval_top(self, data):
        self.result = confidence_interval_top(data)
        return self.result

    def correlation_coefficient(self, data, data1):
        self.result = correlation(data, data1)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def p_value(self, data):
        self.result = p_value(data)
        return self.result

    def population_mean(self, data):
        self.result = population_mean(data)
        return self.result

    def proportion(self, data):
        self.result = proportion(data)
        return self.result

    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def population_proportion_variance(self, data):
        self.result = variance_of_population_proportion(data)
        return self.result

    def z_score(self, data):
        self.result = z_score(data)
        return self.result
