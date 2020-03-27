from Calculator.Multiplication import multiplication
from Calculator.Division import division


def cochran(p, q, z, e):
    try:
        n1 = multiplication(p, p)
        n2 = z * z
        n3 = multiplication(n1, n2)
        n4 = e * e
        nCochran = division(n4, n3)
        return int(nCochran)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")

# https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/find-sample-size/
