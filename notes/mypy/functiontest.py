def greet(names: list[str]) -> None:
    for name in names:
        print(f"Hello, {name}!")


greet(["Alice", "Bob"])  # Fine
greet("hello")  # Mypy will flag this as an error