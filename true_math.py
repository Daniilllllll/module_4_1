from math import inf
def divide2(first, second):
    try:
        j = first/second
    except ZeroDivisionError:
        j = inf
    else:
        j = first/second

    return j