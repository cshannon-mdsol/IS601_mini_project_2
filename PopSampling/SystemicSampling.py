from Random.GenNumberSeed import GenNumberSeed


class SystematicSampling:

    @staticmethod
    def systematic_sampling(series):
        size = len(series)
        number = round((GenNumberSeed.rand_num(size, 2, size))/4)
        if number == 1:
            number = 3
        series2 = []
        temp = number - 1
        while temp <= size-1:
            value = series[temp]
            series2.append(value)
            temp += number
        return series2
