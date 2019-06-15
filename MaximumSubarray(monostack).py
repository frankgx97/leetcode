class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = max(nums)
        for i in range(len(nums)):
            if i > 0:
                nums[i] += nums[i-1]
        stack = [0]
        for i in range(len(nums)):
            if not stack or stack[-1] < nums[i]:
                stack.append(nums[i])
                r = max(r, nums[i] - stack[0])
            else:
                while(stack and stack[-1] > nums[i]):
                    stack.pop()
                stack.append(nums[i])
        return r
