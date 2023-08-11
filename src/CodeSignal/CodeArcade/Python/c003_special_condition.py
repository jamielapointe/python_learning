"""Determine which comparison is different from the rest
"""
a = True
b = False

# The following is not valid Python syntax
# if a == not b:
#     print('a == not b')
# else:
#     print('a != not b')

if not (a == b):  #  pylint: disable=unneeded-not, superfluous-parens
    print('not(a==b)')
else:
    print('not(a!=b)')

if not a == b:  #  pylint: disable=unneeded-not
    print('not a==b')
else:
    print('not a!=b')

if a == (not b):
    print('a==(not b)')
else:
    print('a!=(not b)')
