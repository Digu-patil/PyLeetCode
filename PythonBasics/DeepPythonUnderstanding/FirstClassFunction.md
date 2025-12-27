# What are First Class Functions in Python?
1. Functions can be passed as an argument.
2. Functions can be assigned as variables
3. Functions can be returned from another function.

## Understanding Closures
1. Here we try to tell what encloses the scope of a variable
2. If a variable is local or is part of an enclosing scope of another function

```python
# Example 1

def outer():
    x = 10
    def inner():
        print(x)
    return inner

# We can see inner has closures
f = outer() # not that inner is stored in f
print(f.__closure__) 
# (<cell at 0x000001AD304E1480: int object at 0x00007FFF05DD4AD8>,)
print(f.__closure__[0].cell_contents) # 10

'''
This is a closure, as "x" is not being assigend in "inner", but "x" is used from an enclosing scope of "outer"
'''
```

```python
# Example 2

def outer():
    x = 10
    def inner():
        x = x+1   # As assignment is done here this would through an error
        print(x)
    return inner
outer().__closure__ # None

'''
Here as we are assigning "x" in the inner function as well, it acts as a local variable to inner
Error - UnboundedLocal
This can be fixed by saying nonlocal x, which says that x is not a local variable
'''
```