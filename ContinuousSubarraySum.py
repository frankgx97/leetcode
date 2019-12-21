class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        prefix sum
        corner case: k = 0 or all items in num = 0
        time O(n^2)
        '''
        for i in range(1,len(nums)):
            nums[i] = nums[i-1]+nums[i]
        nums = [0]+nums
        for i in range(len(nums)-2):
            for j in range(i+2,len(nums)):
                if ((nums[j] - nums[i]) == 0 and k==0) or (k!=0 and (nums[j] - nums[i])%k == 0):
                    return True
        return False
