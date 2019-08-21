class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        i=0
        while i <= len(nums)-1:
            if nums[i] not in d.keys():
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

            if d[nums[i]] > 2:
                nums.pop(i)
            else:
                i += 1
        return
