def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    
    ## base/corner cases
    if number < 0:
        warn = "Number must be non-negative, else returns None."
        print(warn)
        return None

    if number == 1 or number == 0:
        return number

    else:
        return sqrt_helper(1, number, number)

def sqrt_helper(low, high, ans):
    """ recursive function uses binary search
        It recursively finds mid and compare its square value with ans.
    """

    mid = (low + high)//2
    mid_sqr = mid*mid

    ## Indicates no more recursion needed
    if low == mid:
        return mid

    ## Compare mid-sqr value with ans and accordingly finds new mid
    if mid_sqr == ans:
        return mid
    elif mid_sqr > ans:
        return sqrt_helper(low, mid, ans)
    else:
        return sqrt_helper(mid, high, ans)



### Testcases

# Edge cases: 
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (None == sqrt(-1)) else "Fail") # return None and prints: number must be non-neg

## Perfect squares
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1024 == sqrt(1048576)) else "Fail")

## Non=prefect squares
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (10 == sqrt(120)) else "Fail")
print ("Pass" if  (11 == sqrt(122)) else "Fail")
print ("Pass" if  (1000 == sqrt(1000005)) else "Fail")
