class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        brute force - ac
        '''
        if not nums:
            return []
        i=0
        j=i+k
        m = []
        while j<=len(nums):
            m.append(max(nums[i:j]))
            i+=1
            j+=1
        return m
