from Statistics.ZScore import z_score
from PopSampling.MarginError import MarginError
from Calculator.Square import square


class UnkSampleSize:

    @staticmethod
    def unk_sample_size(nut, data, percentage):
        z = ZScore.z_score(nut, data)
        e = MarginError.margin_error(nut, data)
        p = percentage
        q = 1 - p
        val = z/e
        sample = Square.square(val, 2) * p * q
        return sample
