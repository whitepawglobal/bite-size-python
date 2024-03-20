

def fibonacci():
    
    a, b = 0, 1
    
    yield a
    yield b
    
    while True:
        
        
        if a > 100:
            break
            
        a,  b = b, a + b
        
        # equivalent to above
#         temp = b
        
#         b = a + b
#         a = temp
        
        yield b
        
        
        
if __name__ == "__main__":
        
    for val, finval in enumerate(fibonacci()):
        
        print(f"{val} {finval}")