# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            curr = (l+r)//2
            if guess(curr) == 0:
                return curr
            elif guess(curr) == -1:
                r = curr - 1
            elif  guess(curr) == 1:
                l = curr + 1
        return -1
