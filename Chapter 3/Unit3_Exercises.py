def applyEachTo(L, x):
    '''
    This function apply is function in L list with x parameter and return a list back.
    :param L: List of the functions
    :param x: Parameter for functions. Type: alle
    :return: List of the functions values
    '''
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1