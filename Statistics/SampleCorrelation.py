from Statistics.ZScore import z_score
from Statistics.Mean import mean
from Calculator.Multiplication import multiplication
from Calculator.Subtraction import subtraction
from Calculator.Square import square
from Calculator.Division import division
from Calculator.SquareRoot import square_root
from pprint import pprint
import numpy as np


def sample_correlation(data, data1):
    try:



        mean1 =mean(data)
        mean2 =mean(data1)
        List1=[]
        List2=[]

        for num in data:
            a = subtraction(int(round(mean1,0)),num)
            List1.append(a)

        for num in data1:
            b = subtraction(mean2,num)
            List2.append(b)
        c = np.multiply(List1, List2)
        cc=0
        for num in c:
            cc= cc+num

        d=0
        e=0
       # pprint(List1)
       # pprint(List2)
        for num in List1:
            d = d+ square(num)
        for num in List2:
            e = e +square(num)

        f = multiplication(int(d), e)
        g = square_root(int(f))
        h = division(int(g),cc)
        pprint(float(cc))
        pprint(e)
        pprint(f)
        pprint(float(g))
        pprint(str(round(h,9)))
        nCorrelation = round(h,9)
        pprint(nCorrelation)
        return nCorrelation
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/correlation-coefficient-formula/
# https://www.mathsisfun.com/data/correlation.html
# https://www.geeksforgeeks.org/numpy-subtract-in-python/