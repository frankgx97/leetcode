class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, vi in enumerate(nums):
            for j in range(i+1, len(nums)):
                if vi + nums[j] == target:
                    return [i, j] 