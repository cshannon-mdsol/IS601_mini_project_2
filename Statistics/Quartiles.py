from Statistics.Median import median
from Calculator.Addition import addition


def quartiles(data):
    try:
        List2 = []
        num_values = len(data)
        nNum = float(num_values)
        Q2 = median(data)

        nSort = sorted(data)
        a = .25 * nNum
        b = .75 * nNum

        for num in nSort:
            List2.append(num)

        Q1 = List2[int(a)]
        Q3 = List2[int(b)]
        bb = addition(addition(int(Q1), int(Q2)), int(Q3))
        return int(Q1), int(Q2), int(Q3)
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

#     https://www.statisticshowto.datasciencecentral.com/what-are-quartiles/
#      https://www.mathsisfun.com/data/quartiles.html
