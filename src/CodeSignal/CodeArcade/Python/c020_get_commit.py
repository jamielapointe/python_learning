''' Get Commit

#pylint: disable=line-too-long
Source: https://app.codesignal.com/arcade/python-arcade/slithering-in-strings/FmSEJMu8fbybQ7Ka4
#pylint: enable=line-too-long

The Abanamama Version System (AVS) is a software versioning and revision
control system used in highly secure environments. In this system, each
commit is assigned a unique name, the first part of which consists of the
username encrypted in the base-4 system using symbols '0', '?', '+', and '!',
and the second part consists of symbols of English alphabet.

Given such commit, your task is go remove the username part from it and return
the second part as an answer.

Example

For commit = "0??+0+!!someCommIdhsSt", the output should be
solution(commit) = "someCommIdhsSt".

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string commit

Commit in the format given above. Note, that it is possible that it doesn't
contain the first or the second part.

Guaranteed constraints:
5 ≤ commit.length ≤ 45.

[output] string

The second part of the commit.
'''


def solution(commit):
    return ''.join([c for c in commit if c.isalpha()])


print(solution('0??+0+!!someCommIdhsSt'))
print(solution('noAUTHORnoCOMMITter'))
print(solution('?????!+0??+fgfgdfgdg'))
print(solution('???!+?+?+?+'))
print(solution(''))
