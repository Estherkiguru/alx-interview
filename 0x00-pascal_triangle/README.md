# Pascal's Triangle

This project implements Pascal's Triangle in Python. The goal is to create a function that generates Pascal's Triangle up to a specified number of rows.

## Description

Pascal's Triangle is a triangular array of the binomial coefficients. The rows of Pascal's Triangle are conventionally enumerated starting with row `n = 0` at the top. The entries in each row are the coefficients of the binomial expansion of `(a + b)^n`.

## Function Prototype

```python
def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists containing integers representing Pascal's Triangle.
    """

