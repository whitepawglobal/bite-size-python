from typing import Union

#from python 3.10 onwards
def simplefunc2(input : str | None = None):

    print(f"simple func2: {input}")


# older than python 3.10
# backward dependency makes this works too for version after python 3.10
def simplefunc1(input : Union[str, None] = None):

    print(f"simple func1: {input}")


if __name__ == "__main__":

    input = "hello world"

    simplefunc1(input)
