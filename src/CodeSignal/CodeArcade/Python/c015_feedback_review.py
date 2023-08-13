''' Feedback Review

#pylint: disable=line-too-long
Source: https://app.codesignal.com/arcade/code-arcade/python-arcade/meet-python/8rCFf6Q5KAdYHJs48
#pylint: enable=line-too-long

You've launched a revolutionary service not long ago, and were busy improving
it for the last couple of months. When you finally decided that the service is
perfect, you remembered that you created a feedbacks page long time ago, which
you never checked out since then. Now that you have nothing left to do, you
would like to have a look at what the community thinks of your service.

Unfortunately it looks like the feedbacks page is far from perfect: each
feedback is displayed as a one-line string, and if it's too long there's no way
to see what it is about. Naturally, this horrible bug should be fixed. Implement
a function that, given a feedback and the size of the screen, splits the
feedback into lines so that:

each token (i.e. sequence of non-whitespace characters) belongs to one of the
lines entirely;
each line is at most size characters long;
no line has trailing or leading spaces;
each line should have the maximum possible length, assuming that all lines
before it were also the longest possible.
Example

For feedback = "This is an example feedback" and size = 8,
the output should be

solution(feedback, size) = ["This is",
                            "an",
                            "example",
                            "feedback"]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string feedback

A string containing a feedback. Each feedback is guaranteed to contain only
letters, punctuation marks and whitespace characters (' ').

Guaranteed constraints:
0 ≤ feedback.length ≤ 100.

[input] integer size

The size of the screen. It is guaranteed that it is not smaller than the
longest token in the feedback.

Guaranteed constraints:
1 ≤ size ≤ 100.

[output] array.string

Lines from the feedback, split as described above.
'''

import textwrap


def solution(feedback, size):
    return textwrap.wrap(feedback, size)


print(solution('This is an example feedback', 8))
print(solution('This is an example feedback', 40))
print(solution('', 10))
print(solution('Dude, do you even review these feedbacks?', 16))
