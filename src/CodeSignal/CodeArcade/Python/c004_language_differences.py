"""Demonstrate the difference between "integer division" in Python and C++.
"""


def division(x: int, y: int) -> int:
    """Perform integer division of x by y
    In Python, integer division is performed using the // operator
    Integer division is really floor division in Python!
    This makes a difference when x or y is negative.
    In C++, integer division is performed using the / operator.
    """
    return x // y


print(division(5, 2))
print(division(5, -2))  # in C this is -2 and Python this -3
print(division(-5, 2))  # in C this is -2 and Python this -3
print(division(-5, -2))
print(division(-8, 2))
print(division(-10, -3))
print(division(5, 10))
print(division(17, 13))
print(division(15, -4))  # in C this is -3 and Python this -4
