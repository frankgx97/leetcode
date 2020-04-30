class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)):
            if i > mx:
                return False
            else:
                mx = max(mx, i+nums[i])
                if mx >= len(nums)-1:
                    return True
        return True
