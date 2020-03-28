from Statistics.ZScore import z_score


def pop_correlation(data, data1):
    try:

        zScore1 = z_score(data)
        zScore2 = z_score(data1)
        zScore1_zScore2 = list(map(lambda x, y: x * y, zScore1, zScore2))
        correlate = sum(zScore1_zScore2) / len(zScore1_zScore2)
        return round(correlate, 7)

    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://mathcracker.com/correlation-coefficient-calculator-using-z-score
