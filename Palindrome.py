#The most elegant solution to this would be to sclice a string

'''
x = 121

#convert the number to a string
num_string = str(x)
if x == num_string[::-1]:
    print(x,' is a Palindrome')
else :
    print(x,' is not a Palindrome')

'''

# Let's say we are not allowed to use slicing
# we can think of swaping the characters and numbers


n = -123456
reversed = 0
sign = -1 if n < 0 else 1
while n != 0 :
    # print('Press enter to loop in', input())
    individual_digts = int(n%10) # take the remainder
    # print('digit is ',individual_digts)
    reversed = reversed * 10 + individual_digts
    # print('reversed is ', reversed)
    n = int(n/10)
print(reversed)

