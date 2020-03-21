from Statistics.Zscore import Zscore
from PopSampling.MarginError import MarginError
from Statistics.StandardDeviation import StandardDeviation
from Calculator.Square import square


class PopSampleSize:

    @staticmethod
    def pop_sample_size(nut, data):
        e = MarginError.margin_error(nut, data)
        stddev = StandardDeviation.stddev(data)
        val = (1.96 * stddev) / e
        sample = Square.square(val, 2)
        return sample
