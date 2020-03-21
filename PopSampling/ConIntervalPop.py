from numpy import sem, t
from Statistics.Mean import mean


class ConfidenceIntervalPop:

    @staticmethod
    def confidence_interval_pop(conf, data):
        length = len(data)
        mean = mean.mean(data)
        std_err = sem(data)
        high = std_err * t.ppf((1 + conf) / 2, length - 1)
        start = mean - high
        end = mean + high
        return start, end
