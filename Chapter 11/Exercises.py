def int_to_str(i):
    """
    Assumes i non negative integer
    Return a decimal string representation i
    """
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i>0:
        result = digits[i%10] + result
        i= i//10
    return result
int_to_str(30)