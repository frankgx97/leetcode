class Solution:
    def rob(self, nums: List[int]) -> int:
        def r(nums, index):
            if index < 0:
                return 0
            else:
                return max(r(nums,index-2)+nums[index], r(nums,index-1))
        return r(nums, len(nums)-1)
