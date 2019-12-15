class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        time: O(n)
        space: O(n)
        '''
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] in dic and dic[target - nums[i]] != i:
                return [dic[target - nums[i]],i]
