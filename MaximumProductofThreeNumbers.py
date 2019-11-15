class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        '''
        sort - ac
        corner case
        1. 0
        2. negative
        '''
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
