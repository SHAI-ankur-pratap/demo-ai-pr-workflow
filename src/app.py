"""
Simple calculator app — reviewed by AI on every PR from every fork.
"""
import math


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


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def square_root(a: float) -> float:
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)


def logarithm(a: float, base: float = math.e) -> float:
    if a <= 0:
        raise ValueError("Cannot take log of zero or negative number")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(a, base)


def calculate(operation: str, a: float, b: float = None) -> float:
    unary_ops = {
        "sqrt": square_root,
    }
    binary_ops = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "power": power,
        "modulo": modulo,
        "log": logarithm,
    }
    if operation in unary_ops:
        return unary_ops[operation](a)
    if operation in binary_ops:
        if b is None:
            raise ValueError(f"Operation '{operation}' requires two arguments")
        return binary_ops[operation](a, b)
    all_ops = sorted(list(unary_ops.keys()) + list(binary_ops.keys()))
    raise ValueError(f"Unknown operation: '{operation}'. Choose from: {all_ops}")


if __name__ == "__main__":
    print(calculate("add", 10, 5))         # 15.0
    print(calculate("divide", 10, 2))      # 5.0
    print(calculate("power", 2, 8))        # 256.0
    print(calculate("sqrt", 16))           # 4.0
    print(calculate("log", 100, 10))       # 2.0
