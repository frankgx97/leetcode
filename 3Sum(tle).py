class Solution:     
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(target, index):
            temp_result = []
            for i in range(index, len(nums)):
                if (target - nums[i]) in nums[i+1:]:
                    temp_result.append([-target, nums[i], target - nums[i]])
            return temp_result

        result = []
        duplicate = []
        for i in range(len(nums)):
            for j in two_sum(-nums[i], i+1):
                if sorted(j) not in duplicate:
                    result.append(j)
                    duplicate.append(sorted(j))
        return result
