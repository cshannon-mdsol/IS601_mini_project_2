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

    

    def mean(self, data):
        self.result = mean(data)
        return self.result
