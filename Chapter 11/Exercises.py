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

def gen_powerset(L):
    """
    Assumes L is a list 
    Returns a list of lists that contains all possible combinations of the elements of L.
    E.g. if L is [1,2] it will return a list with elements [],[1][2] and [1,2]
    """
    powerset= []
    for i in range(0, 2**len(L)):
        bin_str = get_binary_rep(i,len(L))
        subset = []
        for j in range(len(L)):
            if bin_str[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset

print(gen_powerset([1,2,3,4]))