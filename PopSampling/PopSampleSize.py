from Statistics.ZScore import z_score
from PopSampling.MarginError import MarginError
from Statistics.StandardDeviation import stddev
from Calculator.Square import square


class PopSampleSize:

    @staticmethod
    def pop_sample_size(nut, data):
        e = MarginError.margin_error(nut, data)
        nstddev = stddev(data)
        val = (1.96 * nstddev) / e
        sample = Square.square(val, 2)
        return sample
