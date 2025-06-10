'''
Problem Statement
1. Given a value A and B
2. Find a exponent value of A that is close to B
3. if A = 2 and B = 9
4. Then Ouptut should be 8 as 2^3 = 8
'''

'''
Solution 1 - Brute Force
1. Try to get the exponent value first, by taking the log of B to the base A
2. Convert the log value to an integer , say x
3. Create and upper and lower bound by createing A**X adn A**(X+1)
4. Check wich one is near to B an return that
'''

import math

def NearestExponentValue(val1, val2):
    lb_exponent = int(math.log(val2, val1))
    lb = val1**lb_exponent
    ub = val1**(lb_exponent+1)
    # Check which bound is near to val2
    if abs(val2 - lb) <= abs(val2-ub):
        return lb
    else:
        return ub


'''
Solution 2 - If we are not allowed to use Math library
1. create a var to check the value of each power
2. compare it with the val2
'''

def NearestExponentValue(val1, val2):
    exp = 1
    num = val1
    while num < val2:
        num = num**exp
        exp += 1
    lb = val1**(exp-2)
    ub = val1**(exp-1)
    # Check which bound is near to val2
    if abs(val2 - lb) <= abs(val2-ub):
        return lb
    else:
        return ub    

'''
Test Cases
'''

print(NearestExponentValue(2,4))
print(NearestExponentValue(2,5))
print(NearestExponentValue(2,6))
print(NearestExponentValue(2,7))
print(NearestExponentValue(2,15))

