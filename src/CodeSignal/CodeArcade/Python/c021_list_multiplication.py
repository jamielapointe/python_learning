''' List Multiplication

#pylint: disable=line-too-long
Source: https://app.codesignal.com/arcade/python-arcade/lurking-in-lists/FBsDp8XJZrKNPEEmq
#pylint: enable=line-too-long

You have come across the following piece of code:
`c = a * b`

Could the following be possible outcomes:

1. `c` equals `a` repeated `b` times;
2. `c` equals `b` repeated `a` times;
'''


def test0():
    a = [1, 2, 3]
    b = 3
    c = a * b
    print(c)


def test1():
    a = 3
    b = [1, 2, 3]
    c = a * b
    print(c)


test0()
test1()
