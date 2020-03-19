from Statistics.ZScore import z_score
from Statistics.Mean import mean
from Calculator.Multiplication import multiplication
from Calculator.Subtraction import subtraction
from Calculator.Square import square
from Calculator.Division import division
from Calculator.SquareRoot import square_root
from pprint import pprint



def sample_correlation(data, data1):
    try:
        mean1 = mean(data)
        mean2 = mean(data1)
        pprint(float(mean1))
        a = subtraction(data,mean1)
        b = subtraction(data1,mean2)
        pprint(a)
        c = multiplication(a,b)
        d = square(a)
        e = square(b)
        f=multiplication(d,e)
        g=square_root(f)
        h=division(c,g)
        i=0

        return h
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")

# https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/correlation-coefficient-formula/
# https://www.mathsisfun.com/data/correlation.html