class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        while True:
            if i > length - 1:
                break
            if nums[i] == 0:
                for j in range(i,len(nums)-1):
                    nums[j] = nums[j+1]
                nums[-1] = 0
                length -= 1
                i -= 1
            i += 1
