"""Base conversion
Implement the missing code, denoted by ellipses. You may not modify the pre-
existing code.
Your university professor decided to have a little fun and asked the class to
implement a function that, given a number n and a base x, converts the number
from base x to base 16. To make things more interesting, he announced that the
first student to write the solution will have to answer fewer question than the
rest of the class during the final exam.

Laughing devilishly, you asked if it was okay to use a language of your choice,
and the unsuspecting professor answered "yes". It's settled then: Python is
your language of choice!

Now you're bound to win. Implement a function that, given an integer number n
and a base x, converts n from base x to base 16.

Example

For n = "1302" and x = 5, the output should be
solution(n, x) = "ca".

Here's why:
13025 = 20210 = ca16.
"""


def solution(n: str, x: int) -> str:
    return hex(int(n, x)).replace("0x", "", 1)


print(solution("1302", 5))
print(solution("1010101", 2))
print(solution("z", 36))
print(solution("30", 4))
print(solution("6", 7))
print(solution("337", 8))
print(solution("ab3f", 16))
print(solution("0", 2))
print(solution("ci", 19))
print(solution("8c4897", 13))
