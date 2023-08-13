''' Remove Tasks

#pylint: disable=line-too-long
Source: https://app.codesignal.com/arcade/python-arcade/lurking-in-lists/L3TQWdGMcWL85LHcR
#pylint: enable=line-too-long

Implement the missing code, denoted by ellipses. You may not modify the pre-
existing code.

Today is a good day: it's the kth year since you started to work at the
company, which means you have to have a party today. In order to get home
earlier and prepare for the jamboree, you need to get home early. You
decided to remove each kth tasks from your toDo list, since today is your
day and you can do whatever you please.

Given the list of task ids in your toDo list, remove each kth task from it
and return the list of remaining tasks.

Example

For k = 3 and toDo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22],
the output should be
solution(k, toDo) = [1237, 2847, 2947, 1, 374827, 22].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer k

Guaranteed constraints:
1 ≤ k ≤ 30.

[input] array.integer toDo

Ids of the tasks in your to-do list.

Guaranteed constraints:
1 ≤ toDo.length ≤ 100,
1 ≤ toDo[i] ≤ 4 · 105.

[output] array.integer
'''


def solution(k, todo):
    del todo[k - 1::k]
    return todo


print(solution(3, [1237, 2847, 27485, 2947, 1, 247, 374827, 22]))
