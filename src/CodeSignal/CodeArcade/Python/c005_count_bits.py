"""Count bits in an integer
"""


def solution(n: int) -> int:
    """Count the number of bits in an integer
    Another way to do this is: log2(n) + 1
    """
    return n.bit_length()


print(solution(50))
print(solution(1))
print(solution(8))
print(solution(37))
print(solution(0))
print(solution(100))
print(solution(524288))
print(solution(1024))
print(solution(1023))
print(solution(2**20))
print(solution(2**30))
print(solution(2**40))
print(solution(2**50))
print(solution(2**60 - 1))
print(solution(1000000000))
print(solution(237487384))
print(solution(278))
