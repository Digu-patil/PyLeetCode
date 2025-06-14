'''
Problem Statement - 
We need to check if the value provided to the function is within 2 of a multiple of 10
i.e 22 is within 2 of (2 times 10)
19 is within 2 of 1 of (2 times of 10)
'''

def NearToTen(N):
    if N % 10 == 0:
        return True
    ct = 1
    lb = N
    ub = N
    while ct <= 2:
        lb += 1
        ub -= 1
        if (lb % 10 == 0) or (ub % 10 == 0):
            return True
        ct += 1
    return False

'''Test Cases'''

print(NearToTen(5))
print(NearToTen(10))
print(NearToTen(22))
print(NearToTen(23))
print(NearToTen(19))
