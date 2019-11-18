import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        mono stack
        '''
        m = max(nums) #to handle mono-decrease input
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        stack = [0] #to handle mono-increase input
        
        
        for i in nums:
            if not stack or i > stack[-1]:
                stack.append(i)
                m = max(m,stack[-1] - stack[0])
            else:
                curr = 0
                while stack and i <= stack[-1]:
                    curr = i - stack.pop(-1)
                stack.append(i)
                
        return m
