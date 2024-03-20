
def do_twice(func):
    
    @functools.wraps(func)
    def wrapper():
        
        func()
        func()
        
    return wrapper


def do_twice_with_arg(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        func(*args, **kwargs)
        func(*args, **kwargs)
        
    return wrapper


def do_with_return(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        func(*args, **kwargs)
        func(*args, **kwargs)
        
        return "TESTING 123"
        
    return wrapper