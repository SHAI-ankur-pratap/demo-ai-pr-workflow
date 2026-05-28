"""
Simple calculator app — this is the "codebase" that AI reviews when PRs are opened.
"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    return base ** exponent


def calculate(operation: str, a: float, b: float) -> float:
    ops = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "power": power,
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}. Choose from {list(ops.keys())}")
    return ops[operation](a, b)


if __name__ == "__main__":
    print(calculate("add", 10, 5))       # 15.0
    print(calculate("divide", 10, 2))    # 5.0
    print(calculate("power", 2, 8))      # 256.0
