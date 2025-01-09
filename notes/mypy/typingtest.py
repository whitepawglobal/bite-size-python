from typing import List

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

add_numbers([1, 2, 3])  # This is fine
add_numbers(["1", "2", "3"])  # Mypy will complain!