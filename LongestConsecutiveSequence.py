class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        sorting - ac
        '''
        if len(nums) == 0:
            return 0
        nums.sort()
        r = 1
        consect = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                consect+=1
                r = max(r,consect)
            elif nums[i] == nums[i-1]:
                continue
            else:
                consect = 1
        return r
