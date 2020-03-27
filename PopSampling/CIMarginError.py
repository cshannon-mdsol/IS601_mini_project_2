import numpy as np
import scipy.stats as st
from pprint import pprint

from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.SquareRoot import square_root

def cimarginerror(n,x,s):
    try:
        zValue = 1.96
        n1 = square_root(n)
        n2=division(n1,s)
        n3=multiplication(n2,zValue)
        return round(float(n3),2)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")
#https://www.dummies.com/education/math/statistics/how-to-calculate-the-margin-of-error-for-a-sample-mean/

    #a = 1.0 * np.array(data)
    #n = len(a)
    #m, se = np.mean(a), st.sem(a)
    #h = se * st.t.ppf((1 + confidence) / 2., n-1)