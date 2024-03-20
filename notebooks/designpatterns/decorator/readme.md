## Boilerplate template for decorator

- decorator is a wrapper function that takes another function  
and extends the behavior of the latter function
- can put the `decorator` function into file and reuse
```
import functools

def decorator(func):

    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):

        # Do something before 

        value = func(*args, **kwargs)

        # Do something after 

        return value

    return wrapper_decorator 
```

<img src="sample.png">

- [Decorator with argument](decorator_with_argument.ipynb)
- [Decorator with optional argument](https://realpython.com/primer-on-python-decorators/#creating-decorators-with-optional-arguments)

## Sample Application

- [Check time performance](time_perforamnce.ipynb)
- [Debugging](debugging_code.ipynb)
- Authenticating Users
  - Use wrapper to check whether user is authenticated , if yes proceed with `func`,
  - Normally the decorators does not need to be own and its written by the web framework (Flask, FastAPI, ...)


## Nesting Decorator
- Executed in the order they are placed
```
>>> from decorators import debug, do_twice

>>> @debug
... @do_twice
... def greet(name):
...     print(f"Hello {name}")
...
```
