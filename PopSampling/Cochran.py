from Statistics.ZScore import z_score
from PopSampling.MarginError import MarginError
#from Statistics.PopulationProportion import PopulationProportion
from Calculator.Square import square


class Cochran:

    @staticmethod
    def cochran(nut, data, realm):
        z = ZScore.z_score(data)
        p = 0#PopulationProportion.pop_proportion(nut, data, realm)
        e = MarginError.margin_error(nut, data)
        q = 1 - p
        cochran = (Square.square(z, 2) * p * q)/Square.square(e, 2)
        return cochran
