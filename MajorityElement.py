class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {}
        for i in nums:
            if i in mapping.keys():
                mapping[i] += 1
            else:
                mapping[i] = 1
        for i in mapping.keys():
            if mapping[i] > len(nums)/2:
                return i
