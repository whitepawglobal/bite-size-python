from memory_profiler import profile
from random import randint

@profile
def run():
    
    a = []#range(len(100))
              
    for i in range(10):
        
        a.append(randint(0, 100))
             
    a.sort()
                 
    print(a)
                 
                 
if __name__ == "__main__":
    
    run()
             
