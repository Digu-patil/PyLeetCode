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

'''
Palindrome Check for string without string sclicing
'''


def easy_pythonic_way(name):
    print(name[::-1])

def rev_str(name):
    reversed_str = ''
    for char in name:
        reversed_str = char + reversed_str
    return reversed_str

def while_loop(name):
    name = list(name)
    start = 0
    end = len(name) - 1
    while (start < end):
        temp = name[start]
        name[start]= name[end]
        name[end] = temp
        start +=1
        end -=1
    return name

name = 'Digvijay'

print(easy_pythonic_way(name))
print(rev_str(name))
print(while_loop(name))



strings = 'abcde'
rev = ''
for i in strings:
    rev = i + rev
    print(rev)
