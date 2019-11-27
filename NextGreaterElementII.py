class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        double length array and monostack - ac
        double the array, and use monostack the same as  Next Greater Element I
        to improve performance, we can break the loop once reach the max item in the array in the extra part.
        in mono stack and dict, store the array index instead of the value to handle the case that duplicated entries exist in the array.
        '''
        stack = []
        dic = {}
        numlength = len(nums)
        nums = nums+nums
        max_in_array = 0
        
        for i in range(len(nums)):
            max_in_array = max(max_in_array,nums[i])
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
            else:
                while stack and nums[stack[-1]] < nums[i]:
                    if stack[-1] not in dic:
                        dic[stack.pop(-1)] = nums[i]
                    else:
                        stack.pop(-1)
                stack.append(i)
            if i > numlength-1 and nums[i] == max_in_array:
                break
        while stack:
            dic[stack.pop(-1)] = -1

        r = []
        for i in range(numlength):
            r.append(dic[i])
        return r
