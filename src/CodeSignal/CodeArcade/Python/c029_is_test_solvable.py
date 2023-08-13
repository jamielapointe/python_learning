'''Is Test Solvable

#pylint: disable=line-too-long
Source: https://app.codesignal.com/arcade/python-arcade/lambda-illusions/eP7hJDmLdZym2Kdo3
#pylint: enable=line-too-long

You've been preparing all night for the upcoming test and entered the class
certain that you will ace it. Now that you received the test questions, you
died inside a little: looks like you prepared for the test on a completely
different topic.

You're not even sure if you should bother to answer the questions. You still
have some hope though: it is known that there's a glitch in the test preparing
system, so that if the sum of digits of question ids is divisible by k, the
answer to each question has a 90% probability to be an A.

Given the list of question ids, determine if the sum of their digits is
divisible by k to see if it's worth trying to pass the test.

Example

For ids = [529665, 909767, 644200] and k = 3, the output should be
solution(ids, k) = true.

The sum of digits is

#pylint: disable=line-too-long
(5 + 2 + 9 + 6 + 6 + 5) + (9 + 0 + 9 + 7 + 6 + 7) + (6 + 4 + 4 + 2 + 0 + 0) = 87
which is divisible by 3. Today is your lucky day after all!
#pylint: enable=line-too-long

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer ids

Array of unique question ids.

Guaranteed constraints:
1 ≤ ids.length ≤ 50,
0 ≤ ids[i] ≤ 106.

[input] integer k

The number that causes a glitch in the test preparing system.

Guaranteed constraints:
2 ≤ k ≤ 10.

[output] boolean

true if the total sum of digits in ids is divisible by k, false otherwise.
'''


def solution(ids, k):
    #pylint: disable=unnecessary-lambda-assignment
    digit_sum = lambda n: sum(list(map(int, str(n).strip())))
    #pylint: enable=unnecessary-lambda-assignment

    sm = 0
    for question_id in ids:
        sm += digit_sum(question_id)
    return sm % k == 0


print(solution([529665, 909767, 644200], 3))
print(solution([529665, 909767, 644201], 3))
