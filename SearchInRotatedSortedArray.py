class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        for left in range(0,right+1):
            if nums[left] == target:
                return left
            if left >=1 and nums[left] < nums[left-1]:
                break
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
