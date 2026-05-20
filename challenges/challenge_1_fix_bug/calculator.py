"""A simple calculator module with several bugs for students to fix using Devin."""


class Calculator:
    """Basic arithmetic calculator."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return a minus b."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return a divided by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base: float, exponent: int) -> float:
        """Return base raised to the exponent.

        Must handle negative exponents correctly.
        """
        return float(base ** exponent)

    def average(self, numbers: list[float]) -> float:
        """Return the arithmetic mean of a list of numbers.

        Raises:
            ValueError: If the list is empty.
        """
        if not numbers:
            raise ValueError("Cannot compute average of empty list")
        return sum(numbers) / len(numbers)
