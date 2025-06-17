'''
Problem Statement
1. We want to check if the opening and closing parantheses are matching
    i.e., []{}(), [()]{} is valid, but ][])() this is not valid
'''

'''
Solution 
1. Think of a stack
2. Whenever you see a opening parantheses, add it to the stack
3. Whenever you see a closing parantheses of the same type, remove it from the stack
4. In the end check if the stack is blank if yes then its valid
'''

def ParanthesesBalancer(par_str):
    stack = []
    par_mapping = {')':'(',']':'[','}':'{'}
    for par in par_str:
        if par in ('(','[','{'):
            stack.append(par)
        elif par in (')',']','}'):
            if not stack or stack[-1] != par_mapping[par]:
                return False
            stack.pop()
    return (len(stack)==0)

'''Test Case'''

par_str = '()'
print(ParanthesesBalancer(par_str))