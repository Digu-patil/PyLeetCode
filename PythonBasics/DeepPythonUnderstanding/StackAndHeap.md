# Stack
1. Stack Frame is short lived.
2. It only stores references (pointers) to objects in the heap memory.
3. Note that actual objects are stored on the heap
4. A new stack frame is created for every funciton call

# Heap
1. Actual objects like Integers, floats, strings, lists, dicts, functions, classes, i.e, every object is stored on Heap.
2. Due to heap memory allocation, we have recurssion limit (default 3000 recurssion calls), we can modify the default but not recommended.

# Modules - Global Variables and Functions
1. As stack frame is created for function calls, and is short lived.
2. The question what happens to the global variables?
3. They are stored in the modules object as part of a dictionary.
4. Note that only the references are stored, the actual object still lives inside the heap.

> Jupyter/IPython and Python scripts behave differently when it comes to these storages and garbage collection, this is because jupyter references and keeps track of a lot of input history as it executes cell wise.

> We can use the "sys" module to get deeper understaing how many references have been made to the same object, get the global variable namespace, what is the "recurssion limit"

> We can use the "inspect" module to look for the underlying stackframe and understaing, local, global and builtin scope namespaces

```python
import sys
import inspect

a = 20
b = [20,60,80]

def outer(a):
    x = 10
    outer_frame = inspect.currentframe()
    print(f'Stack frame created for the following function -> {outer_frame.f_code.co_name}')
    print(f'These are local var to outer function -> {outer_frame.f_locals}')
    print(f'These are global var to outer function {outer_frame.f_globals}')

    # We can also access the global variable using the modules object, where they originally live
    print(sys.modules['__main__'].__dict__)
    def inner():
        p = a + x
        inner_frame = inspect.currentframe()
        print(f'Stack frame created for the following function -> {inner_frame.f_code.co_name}')
        print(f'These are local var to inner function -> {inner_frame.f_locals}')
        print(f'These are global var to inner function -> {inner_frame.f_globals}')
        return p
    return inner

b = outer(a)
b()
```

## Important points to note
1. Global variables like, a, b, outer, inspect, sys
    they live on the modules object, consdier the modules object as the stack frame for global scope, 
    they just sotre the pointer/references to the actual object, but the actual object is stored in the heap
```
Stack frame created for the following function -> outer
{'a': 20,
 'outer_frame': <frame at 0x0000028FB8E07AE0, file 'C:\\Users\\imdig\\Desktop\\Learning\\PyLeetCode\\PythonBasics\\DeepPythonUnderstanding\\test.py', line 12, code outer>,
 'x': 10}
These are local var to outer function -> None
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__cached__': None,
 '__doc__': None,
 '__file__': 'C:\\Users\\imdig\\Desktop\\Learning\\PyLeetCode\\PythonBasics\\DeepPythonUnderstanding\\test.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000028FB8C7BCB0>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'a': 20,
 'b': [20, 60, 80],
 'inspect': <module 'inspect' from 'C:\\Program Files\\Lib\\inspect.py'>,
 'outer': <function outer at 0x0000028FB8C3D080>,
 'pprint': <function pprint at 0x0000028FB8FA2700>,
 'sys': <module 'sys' (built-in)>}
```

# sys v/s inspect

We can get the frame object and its contents in two ways
1. sys._getframe() - this is low level, part of CPython implementation, not sure if it would work in PyPy etc.
2. inspect.currentframe() - this is part of public API, and returns none if no frames are available.

> Generally use inspect.currentframe() usually they are the same as sys._getframe()