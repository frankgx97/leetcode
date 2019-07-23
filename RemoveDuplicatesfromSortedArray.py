class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = []
        for i in nums[:]:
            if i not in dup:
                dup.append(i)
            else:
                nums.remove(i)
        return len(nums)
