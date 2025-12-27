# Names in Python
1. Names are just lables
2. Do not mistake them with objects.
3. Rebinding a name does not affect the other.

```python
# Example 1
a = 10
b = a
a = 20 # this is where rebinding occurs
'''
1. 10 is created a an interger object in the memory.
2. Name "a" is bound to the integer object 10.
                a --> 10
3. Name "b" is also bound to the same integer object 10.
                a & b --> 10
4. 20 is created as an integer object in the memory.
5. Name "a" now rebinds and is now bound to the integer object 20
                b --> 10
                a --> 20
'''
```
---
- Please Note that if the same object would have been updated in memory both the variables would still have pointed to the same object
```python
# Example 2
def func(lst):
    lst = [10,20,30]

x = [1,2,3]
print(func(x))

# Output = [1,2,3]

'''
1. A Function object is created in memory
2. Name "func" is bound to that function object
3. A list object is created with the following data in memory [1,2,3]
4. Name "x" is bound to that list object
                x --> [1,2,3]
5. When executing the function object, it creates a local name lst
6. Now as x is provided as an argument to the function object, x and lst point to the same list object
                x & lst --> [1,2,3]
7. A new list object [10,20,30] is created in memory
8. "lst" is now rebinded to the new list object due to the assignment
                x --> [1,2,3]
                lst --> [10,20,30]
'''
```
---
- Following is the example, where the names are not rebinded but still point to the same memory location
```python
# Example 3
def func(lst):
    lst.append(4)

x = [1,2,3]
print(func(x))
# Output - [1,2,3,4]

'''
1. A Function object is created in memory, "func" name is bound to that object.
2. A list object is created, and "x" name is bound to that object
3. Function object execution creates a local name "lst"
4. "lst" and "x" are both by the same list object [1,2,3]
5. **Note that here we are modiying the same list object
6. "lst" is getting modified
7. As "lst" and "x" point the same modified list object.
'''
```