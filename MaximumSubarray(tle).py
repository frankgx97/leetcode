import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = -math.inf
        for i in range(len(nums)):
            if i > 0:
                nums[i] += nums[i-1]
        for i in range(len(nums)):
            if nums[:i]:
                arr = nums[:i]
            else:
                arr = [0]
            r = max(r, nums[i] - min(arr), nums[i])
        return r
