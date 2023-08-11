"""Determine the most efficient comparison
"""
x = 2
y = 3
L = 1
R = 10


def my_pow(x1: int, y1: int) -> int:
    print("my_pow() called")
    return x1**y1


if L < my_pow(x, y) <= R:
    print('L < my_pow(x, y) <= R')

if my_pow(x, y) > L and my_pow(x, y) <= R:
    print('my_pow(x,y) > L and my_pow(x,y) <= R')

if my_pow(x, y) in range(L + 1, R + 1):
    print('my_pow(x,y) in range(L+1, R+1)')
