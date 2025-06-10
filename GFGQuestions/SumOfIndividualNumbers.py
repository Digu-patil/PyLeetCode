'''
Problem Statement 
1. Given a number 43, 99, 121
2. The function should return the sum of te inividual digits
'''

'''
Solution 1 - Brute Force
1. Convert the number into string
2. Iterate through the string
3. Convert the individual numbers back to integer
4. Create a variable, keep summing the integers using a for loop
'''

# Solution 1

# def SumOfDigits(num):
#     num_string = str(num)
#     num_sum = 0
#     for i in num_string:
#         num_sum += int(i)
#     return num_sum

'''
Solution 2 - Mathmetical
1. We would get the last digit using the % operator
2. Add it to the sum
3. Remove the last digit
4. repeat the process until the number is > 0
'''
# Solution 2

def SumOfDigits(num):
    num_sum = 0
    while num > 0:
        digit = num % 10         # Get the last digit
        num_sum += digit         # Add it to the sum
        num = num // 10          # Remove the last digit
    return num_sum


'''
Below are the test cases
'''
print(SumOfDigits(111))
print(SumOfDigits(0))
print(SumOfDigits(100))
print(SumOfDigits(5))

