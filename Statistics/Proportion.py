from Calculator.Division import division


def proportion(num):
    try:
        p_list = list()
        x = sum(num)
        for i in num:
            y = division(i, x)
            p_list.append(y)
        return p_list
    except ZeroDivisionError:
        print("Error - Cannot divide by 0")
    except ValueError:
        print("Error - Invalid data inputs")
