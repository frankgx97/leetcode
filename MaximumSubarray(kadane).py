import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        local_max = -math.inf
        global_max = -math.inf
        
        for i in nums:
            local_max = max(local_max + i, i)
            global_max = max(global_max, local_max)
        return global_max
