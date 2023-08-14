''' Create Spiral Matrix

#pylint: disable=line-too-long
Source: https://app.codesignal.com/arcade/python-arcade/complexity-of-comprehension/HZjrbpxa7gbrmb4kd
#pylint: enable=line-too-long

A spiral matrix is a square matrix of size n × n. It contains all the integers
in range from 1 to n * n so that number 1 is written in the bottom right
corner, and all other numbers are written in increasing order spirally in the
counterclockwise direction.

Given the size of the matrix n, your task is to create a spiral matrix.

Example

For n = 3, the output should be

solution(n) = [[5, 4, 3],
               [6, 9, 2],
               [7, 8, 1]]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

Matrix size, a positive integer.

Guaranteed constraints:
3 ≤ n ≤ 75.

[output] array.array.integer

A spiral matrix of size n.
'''


def solution(n):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    cur_dir = 0
    cur_pos = (n - 1, n - 1)
    res = [[0 for x in range(n)] for x in range(n)]

    for i in range(1, n * n + 1):
        res[cur_pos[0]][cur_pos[1]] = i
        next_pos = cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1]
        if not (0 <= next_pos[0] < n and 0 <= next_pos[1] < n and
                res[next_pos[0]][next_pos[1]] == 0):
            cur_dir = (cur_dir + 1) % 4
            next_pos = cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[
                cur_dir][1]
        cur_pos = next_pos

    return res


print(solution(3))
print(solution(4))
print(solution(5))
