from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.StandardDeviation import stddev
from Statistics.Quartiles import quartiles
from Statistics.Skewness import skewness
from Statistics.SampleCorrelation import sample_correlation
#from Statistics.PopulationCorrelation import population_correlation
from Statistics.ZScore import z_score
from Statistics.MeanDeviation import mean_deviation
from PopSampling.ConIntervalPop import confidence_interval_pop

class PopSampling(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def confidence_interval_pop(self, data):
        self.result = confidence_interval_pop(data1, data2)
        return self.result

    pass
