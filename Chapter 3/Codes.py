#Using bisection search to find log base x

def log_bisection(base,x,epsilon=0.001):
    '''

    :param base: base value of log function
    :param x: log value
    :param epsilon: as a default 0.001
    :return: approximate value of the Log base x value
    '''
    lower_bound=0

    while base**lower_bound<x:
        lower_bound+=1
    lower=lower_bound-1
    high=lower_bound+1
    ans=(high+lower)/2
    while abs(base**ans-x)>=epsilon:
        if base**ans<x:
            lower=ans
        else:
            high=ans
        ans=(lower+high)/2
    return (f'approximate value of log {base} is {ans}')