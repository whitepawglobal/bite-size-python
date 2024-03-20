Built in decorators are just **syntactic sugar**.  
The following two definitions create equal functions 
```
def f(...):
    ...
f = staticmethod(f)

@staticmethod
def f(...):
```

### Static Method

- A static method is a method that belongs to a class rather than an instance of a class.
- To contain logic pertaining to the class, but that logic should not have any need for specific class instance data.
- [Decorator @staticmethod](staticmethod.py)

#### When to use @staticmethod 
- utility function
  ```
    class MathUtils:
        @staticmethod
        def add(x, y):
            return x + y

    # Using the static method
    result = MathUtils.add(3, 4)  # Result: 7
  ```
- **Encapsulation:** 
    - You need to encapsulate a function within a class for better code organization, but the function doesn't rely on instance or class variables. 
    - Static methods provide a way to include such functions within a class without implying any dependency on instance state.
    ```
    class FileOperations:
    @staticmethod
    def read_file(filepath):
        with open(filepath, 'r') as file:
            return file.read()

    # Using the static method
    content = FileOperations.read_file("example.txt")
    ```
- **Namespace Organization**
    - You want to group related functions within a class namespace without implying any specific instance or class dependency. Static methods help in organizing such utility functions within the context of a class.
    ```
    class ValidationUtils:
    @staticmethod
    def is_valid_email(email):
        # Logic to validate email format
        pass

    @staticmethod
    def is_valid_phone_number(phone_number):
        # Logic to validate phone number format
        pass

    # Using static methods for validation
    email_valid = ValidationUtils.is_valid_email("example@example.com")
    phone_valid = ValidationUtils.is_valid_phone_number("123-456-7890")
    ```

### Class Method 
- Bound to the class instead of the function 
  - Example: `Student.from_string(...)` instead of `student.from_string(...)`

#### When to use @classmethod
- Alternative constructors. See example [classmethod.py](classmethod.py)
- Access class variables
    ```
    class MyClass:
    count = 0
    
    def __init__(self):
        MyClass.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

    # Accessing class variable using classmethod
    print(MyClass.get_count())  # Output: 0
    obj1 = MyClass()
    print(MyClass.get_count())  # Output: 1
    ```
- Factory method
    - You want to create instances of subclasses dynamically. Factory methods, which are often implemented using class methods, can help in creating instances of appropriate subclasses based on certain conditions
    ```
    class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_type(cls, shape_type, x, y):
        if shape_type == 'circle':
            return Circle(x, y)
        elif shape_type == 'square':
            return Square(x, y)

    class Circle(Shape):
        pass

    class Square(Shape):
        pass

    # Creating instances using factory method
    circle = Shape.from_type('circle', 0, 0)
square = Shape.from_type('square', 0, 0)
    ```
#### References

- [static factory pattern](https://stackoverflow.com/questions/929021/what-are-static-factory-methods/929273#929273)
- [Decorator @classmethod](classmethod.py)
