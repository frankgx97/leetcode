class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = False
        for i in reversed(range(len(digits))):
            if flag:
                digits[i] += 1
            if i == len(digits) -1:
                digits[i] += 1
            if digits[i] >= 10:
                digits[i] -= 10
                flag = True
            else:
                flag = False
        if flag:
            digits = [1] + digits
        return digits
