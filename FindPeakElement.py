class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        linear scan - ac
        add -inf in both sides of the array
        time O(n)
        '''
        def linear():
            nums = [float('-inf')] + nums + [float('-inf')]
            for i in range(1,len(nums)-1):
                if nums[i-1]<nums[i]>nums[i+1]:
                    return i-1
        
        '''
        binary search - ac
        time O(logn)
        '''
        def bs(nums):
            nums = [float('-inf')] + nums + [float('-inf')]
            left = 1
            right = len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid-1]<nums[mid]>nums[mid+1]:
                    return mid - 1
                elif nums[mid] < nums[mid+1]:
                    left = mid+1
                elif nums[mid-1] > nums[mid]:
                    right = mid - 1
            return 1
        return bs(nums)
