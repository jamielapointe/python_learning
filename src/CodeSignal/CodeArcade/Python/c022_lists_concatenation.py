''' Lists Concatenation

#pylint: disable=line-too-long
Source: https://app.codesignal.com/arcade/python-arcade/lurking-in-lists/FumSx4KegrFbSRdQ4
#pylint: enable=line-too-long

There is a bug in one line of the code. Find it, fix it, and submit.
Given two lists lst1 and lst2, your task is to return a list formed by the elements of lst1 followed by the elements of lst2.

Note: this is a bugfix task, which means that the function is already implemented but there is a bug in one of its lines. Your task is to find and fix it.

Example

For lst1 = [2, 2, 1] and lst2 = [10, 11], the output should be
solution(lst1, lst2) = [2, 2, 1, 10, 11].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer lst1

Guaranteed constraints:
0 ≤ lst1.length ≤ 20,
-106 ≤ lst1[i] ≤ 106.

[input] array.integer lst2

Guaranteed constraints:
0 ≤ lst2.length ≤ 20,
-106 ≤ lst2[i] ≤ 106.

[output] array.integer
'''


def solution(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res


print(solution([2, 2, 1], [10, 11]))
print(solution([], [10, 11]))
print(solution([2, 2, 1], []))
print(solution([], []))
print(solution([1, 2, 3], [4, 5, 6]))
print(solution([1, 2, 3], [4, 5, 6, 7, 8, 9]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6]))
