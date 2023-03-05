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

def add_digits(n):
    """
    Ass
    """
    return 
def get_binary_rep(n, num_digits):
    """
    Asummes n and num_digits are non-negative ints 
    Return a str of length numDigits that is a binary representation of n
    """
    result = ''
    while n>0:
        result = str(n%2) + result
        n = n//2
    if len(result) > num_digits:
        raise ValueError(' not enough digits')
    for i in range(num_digits - len(result)):
        result = '0' + result
    return result
get_binary_rep(30,8)