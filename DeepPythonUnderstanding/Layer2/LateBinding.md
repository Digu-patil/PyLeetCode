# What is Late Binding ?

Late binding occurs when a variable used in a function is looked up when a function is called and not when the function is defined.

```python

func_list = []

for i in range(3):
    func_list.append(lambda:i)

print(func_list[0]()) # prints 2
print(func_list[1]()) # prints 2
print(func_list[2]()) # prints 2
'''
func_list conatins the following things
[<function <lambda> at 0x000001AD3093A2A0>, <function <lambda> at 0x000001AD30939D00>, <function <lambda> at 0x000001AD3093B2E0>]

each of these conatin the lambda function that uses i

Note that the lambda function is not yet executed.
When we call the function in the print statement then the lambda is executed
But it refers to the last value of i which is 2.

This is called late binding
'''
```

Late Binding behaviour would be fixed if the lambada function too was suppoed to be executed immediately, or the value of i was some how sotred within the lambda

This can be done using the default argument

```python

func_list = []

for i in range(3):
    func_list.append(lambda i=i :i)

print(func_list[0]()) # prints 0
print(func_list[1]()) # prints 1
print(func_list[2]()) # prints 2

'''
lambda i=i solves the late binding issue
as default arguments are decided duing function defination, and not during execution.
'''
```