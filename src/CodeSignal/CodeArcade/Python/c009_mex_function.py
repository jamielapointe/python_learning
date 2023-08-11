"""Minimum Excludant (mex) function
You've just started to study impartial games, and came across an interesting
theory. The theory is quite complicated, but it can be narrowed down to the
following statements: solutions to all such games can be found with the mex
function. Mex is an abbreviation of minimum excludant: for the given set s it
finds the minimum non-negative integer that is not present in s.

You don't yet know how to implement such a function efficiently, so would like
to create a simplified version. For the given set s and given an upperBound,
implement a function that will find its mex if it's smaller than upperBound or
return upperBound instead.

Hint: for loops also have an else clause which executes when the loop completes
normally, i.e. without encountering any breaks

Example

For s = [0, 4, 2, 3, 1, 7] and upperBound = 10,
the output should be
solution(s, upperBound) = 5.

5 is the smallest non-negative integer that is not present in s, and it is
smaller than upperBound.

For s = [0, 4, 2, 3, 1, 7] and upperBound = 3,
the output should be
solution(s, upperBound) = 3.

The minimum excludant for the given set is 5, but it's greater than upperBound,
so the output should be 3.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer s

Array of distinct non-negative integers.

Guaranteed constraints:
0 ≤ s.length ≤ 100,
0 ≤ s[i] ≤ 100.

[input] integer upperBound

A positive integer.

Guaranteed constraints:
1 ≤ upperBound ≤ 100.

[output] integer

Mex of s if it's smaller than upperBound, or upperBound instead.
"""


def solution(s: list[int], upper_bound: int) -> int:
    found = -1
    for i in range(upper_bound):
        if not i in s:
            found = i
            break
    else:
        found = upper_bound

    return found


print(solution([0, 4, 2, 3, 1, 7], 10))
print(solution([0, 4, 2, 3, 1, 7], 3))
print(solution([], 13))
print(
    solution(
        [1, 5, 10, 20, 4, 11, 18, 0, 9, 3, 8, 15, 19, 16, 17, 7, 13, 2, 14],
        18))
print(
    solution([
        60, 81, 54, 10, 70, 56, 9, 7, 38, 43, 49, 33, 45, 52, 75, 26, 59, 19,
        35, 12, 30, 36, 41, 79, 6, 53, 24, 63, 5, 20, 76, 62, 34, 78, 67, 8, 18,
        2, 1, 25, 42, 69, 17, 50, 57, 28, 80, 39, 77, 51
    ], 47))
print(
    solution([
        21, 18, 2, 17, 3, 8, 16, 20, 4, 5, 6, 11, 10, 13, 14, 12, 15, 9, 7, 1, 0
    ], 18))
