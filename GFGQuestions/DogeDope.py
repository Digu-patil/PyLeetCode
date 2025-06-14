'''
Assume that everything is in lower case
Problem Statement 1 - 
Given a string you have to count the number of time "doge" appears in the string

Problem Statement 2 - 
Given a string you have to count the number of time "doge" appears, but the g can be 
replaced by any other aplhabet i.e it can be dope, doke etc.
'''

s = 'dogedopedokedonedobedoze'

# P1 - Solution

def DogeCounter(str):
    return str.count("doge")

print(DogeCounter(s))

# P2 - Solution

def AnyDogeCounter(str):
    ct = 0
    for i in range(len(str)-3):
        if s[i] == 'd' and s[i+1] == 'o' and s[i+2].isalpha() and s[i+3] == 'e':
            ct += 1
    return ct

print(AnyDogeCounter(s))

