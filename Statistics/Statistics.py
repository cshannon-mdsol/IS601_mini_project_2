from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
#from Statistics.Variance import variance
#from Statistics.StandardDeviation import stddev
#from Statistics.Quartiles import quartiles
#from Statistics.Skewness import skewness
#from Statistics.SampleCorrelation import sample_correlation
#from Statistics.PopulationCorrelation import population_correlation
#from Statistics.ZScore import z_score
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

    def meandeviation(self, data):
        self.result = mean_deviation(data)
        return self.result

    pass
