from Statistics.ZScore import z_score
#from Statistics.PopulationProportion import PopulationProportion
from Calculator.Square import square
from Calculator.Multiplication import multiplication
from Calculator.Division import division

from pprint import pprint

def cochran(p,q,z,e):
    try:
        n1 = multiplication(p,p)
        n2 = z*z
        n3 =multiplication(n1,n2)
        n4=e*e
        nCochran=division(n4,n3)
        return int(nCochran)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")
#https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/find-sample-size/
#((1.96)2 (0.5) (0.5)) / (0.05)2