class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        iterate k times,
        move the head item to the tail
        '''
        if k > len(nums):
            k -= len(nums)
        for i in range(len(nums)-k):
            nums.append(nums.pop(0))
