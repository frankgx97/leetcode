class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = 0
        count = 0
        for i in nums:
            if count == 0:
                major = i
                count = 1
            elif major == i:
                count += 1
            else:
                count -= 1
        return major
