class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        brute force - tle
        '''
        mx = float('-inf')
        for i in range(len(nums)):
            prod = 1
            for j in range(i,len(nums)):
                prod *= nums[j]
                mx = max(mx, prod)
        return mx
