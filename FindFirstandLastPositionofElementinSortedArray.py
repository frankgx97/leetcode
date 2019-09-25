class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums,target):
            l = 0
            r = len(nums) - 1
            while(l<=r):
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        mid = binary_search(nums,target)
        if mid == -1:
            return[-1,-1]
        left = mid
        right = mid
        flag = 0
        while(nums[left]==nums[mid]):
            if left == 0:
                flag=1
                break
            left-=1
        if not flag:
            left+=1
        flag=0
        while(nums[right]==nums[mid]):
            if right == len(nums)-1:
                flag=1
                break
            right+=1
        if not flag:
            right-=1
        return[left,right]
