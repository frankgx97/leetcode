class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lst = nums
        lo = 0
        hi = len(lst) - 1
        while lo <= hi:
            mid = (lo + hi)//2
            if target == lst[mid]:
                return mid
            if target >= lst[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
