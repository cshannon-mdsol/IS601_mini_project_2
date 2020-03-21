from PopSampling.ConIntervalPop import ConfidenceIntervalPop
from PopSampling.SimpleRandom import SimpleRandom


class ConfidenceIntervalSam(ConfidenceIntervalPop):

    @staticmethod
    def confidence_interval_sam(conf, data, nut, higher):
        sample = SimpleRandom.simple_random(series, realm, nut)
        return ConfidenceIntervalPop.confidence_interval_pop(conf, sample)
