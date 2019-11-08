class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        cumulative sum - tle
        '''
        ans = 0
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i == 0:
                    curr = nums[j]
                else:
                    curr = nums[j] - nums[i-1]
                if curr == k:
                    ans += 1
        return ans
