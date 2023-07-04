from random import randint
from memory_profiler import profile


class DogSlot:
    # defining slots
    __slots__ = ["age"] 
    def __init__(self, age):
        self.age = age


class Dog:
    # defining slots
    def __init__(self, age):
        self.age = age
        
@profile
def dogslot():
    return [DogSlot(age=randint(0, 30)) for _ in range(100000)]


@profile
def dog():
    return [Dog(age=randint(0, 30)) for _ in range(100000)]


if __name__ == "__main__":
    dogslot()
    
    dog()