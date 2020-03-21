from Statistics.StandardDeviation import stddev
from Statistics.ZScore import z_score


class MarginError:

    @staticmethod
    def margin_error(nut, data):
        z_score = ZScore.z_score(nut, data)
        stddev = StandardDeviation.stddev(data)
        return z_score * stddev
