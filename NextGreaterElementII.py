class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        double length array and monostack - ac
        double the array, and use monostack the same as  Next Greater Element I
        to improve performance, we can break the loop once reach the max item in the array in the extra part.
        in mono stack and dict, store the array index instead of the value to handle the case that duplicated entries exist in the array.
        '''
        original_length = len(nums)
        nums = nums+nums
        stack = []
        dic = {}
        for i in range(len(nums)):
            if not stack or nums[i] <= nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[i] > nums[stack[-1]]:
                    dic[stack.pop()] = nums[i]
                stack.append(i)
        while stack:
            dic[stack.pop()] = -1
        r = []
        for i in range(original_length):
            r.append(dic[i])
        return r
                
