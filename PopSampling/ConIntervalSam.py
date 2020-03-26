from PopSampling.ConIntervalPop import confidence_interval_pop
from PopSampling.SimpleRandom import SimpleRandom


def confidence_interval_sam(conf, data, nut, higher):
    sample = SimpleRandom.simple_random(series, realm, nut)
    return confidence_interval_pop(conf, sample)
