'''Word Power

#pylint: disable=line-too-long
Source: https://app.codesignal.com/arcade/python-arcade/complexity-of-comprehension/5rZN7nJ7Tkd9S4TLC
#pylint: enable=line-too-long

You've heard somewhere that a word is more powerful than an action. You decided
to put this statement at a test by assigning a power value to each action and
each word. To begin somewhere, you defined a power of a word as the sum of
powers of its characters, where power of a character is equal to its 1-based
index in the plaintext alphabet (abcdef...wxyz).

Given a word, calculate its power.

Example

For word = "hello", the output should be
solution(word) = 52.

Letters 'h', 'e', 'l' and 'o' have powers 8, 5, 12 and 15, respectively. Thus,
the total power of the word is 8 + 5 + 12 + 12 + 15 = 52.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string word

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ word.length ≤ 25.

[output] integer

Power of the given word.

The solution assumes lower case ASCII characters only, [a-z] == [97-122].
'''

#pylint: disable=consider-using-generator


def solution(word):
    num = {chr(i): i - 96 for i in range(97, 123)}
    return sum([num[ch] for ch in word])


print(solution('hello'))
print(solution('word'))
