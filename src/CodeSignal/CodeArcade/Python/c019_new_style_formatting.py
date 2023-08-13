''' New Style Formatting

#pylint: disable=line-too-long
Source: https://app.codesignal.com/arcade/python-arcade/slithering-in-strings/GADdmPKQivSzQGYLw
#pylint: enable=line-too-long

You came to work in a big company as a Senior Python Developer. Unfortunately
your team members seem to be quite old-school: you can see old-style string
formatting everywhere in the code, which is not too cool. You tried to force
the team members to start using the new style formatting, but it looks like it
will take some time to persuade them: old habits die hard, especially in old-
school programmers.

To show your colleagues that the new style formatting is not that different
from the old style, you decided to implement a function that will turn the
old-style syntax into a new one. Implement a function that will turn the
old-style string formatting s into a new one so that the following two
strings have the same meaning:

s % (*args)
s.format(*args)
Example

For s = 'We expect the %f%% growth this week', the output should be
solution(s) = 'We expect the {}% growth this week'.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s

A correct old-style formatting string. It is guaranteed that each % sign in it
is always followed either by a correct conversion type or by another '%' sign
(see this for reference). It is also guaranteed that it doesn't contain curly
brackets ('{' or '}').

Guaranteed constraints:
1 ≤ s.length ≤ 70.

[output] string

A new-style formatting string without positional indices.d
'''

import re


def solution(s):
    return re.sub(r'(?<!%)((?:%{2})*)%[diouxXeEfFgGcrsan]+', r'\1{}',
                  s).replace(r'%%', r'%')
    # s1 = re.sub(r'(?<!%)((%{2})*)%\w+', r'\1{}', s)
    # s2 = s1.replace(r'%%', r'%')
    # return s2


print(solution(r'We expect the %f%% growth this week'))
print(solution(r'%d%d%%-growth in products is expected quite soon'))
print(solution(r'Much %%s we have here!'))
print(solution(r'Nothing to insert.'))
print(
    solution(r'New style formatting (like %s) is waay cooler than old-style '
             r'(i.e. %s)'))
print(solution(r'%%%%x'))
print(solution(r'%%%%%d'))
print(solution(r'Something %%%%%%%d%%f%%%f here'))

print(solution(r'The stock market fell by -100% in August'))
print(solution(r'We expect the 100%% growth this week'))
