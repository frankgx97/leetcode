class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0]*len(nums)
        r = [0]*len(nums)
        l[0] = 1
        r[len(nums)-1] = 1
        result = []
        prod = 1
        for i in range(1,len(nums)):
            prod *= nums[i-1]
            l[i] = prod
        prod = 1
        for i in reversed(range(0,len(nums)-1)):
            prod *= nums[i+1]
            r[i] = prod
        for i in range(len(nums)):
            result.append(l[i]*r[i])
        return result
